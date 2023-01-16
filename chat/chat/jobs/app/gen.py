import requests
import openai

from config import settings


def generate_voice(text: str):
    query = requests.post(
        url=settings.voice_query_endpoint,
        params={"speaker": 1, "text": text})

    voice_wav = requests.post(
        url=settings.voice_generator_endpoint,
        params={
            "speaker": 1},
        json=query.json(),
        headers={"Content-Type": "application/json"})

    with open('./app/voice/iojdiwajdwa.wav', 'wb') as f:
        f.write(voice_wav.content)


class AIChat:
    def __init__(self):
        # ※冒頭で作成したopenai の APIキーを設定してください
        openai.api_key = settings.gpt_api_key
        self.message = ""

    def response(self, user_input):
        with open("./app/history.txt", 'r') as f:
            self.message = f.read()

        prompt = f"{self.message}\nME:{user_input}"

        # openai の GPT-3 モデルを使って、応答を生成する
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1000,
            temperature=0.7,  # 生成する応答の多様性
            frequency_penalty=0.2,
            presence_penalty=0,
        )

        texts = ''.join([choice['text'] for choice in response.choices])
        print(texts)

        with open("./app/history.txt", 'w') as f:
            f.write(prompt)
            f.write(texts)


if __name__ == "__main__":
    # AIChat のインスタンスを作成する
    chatai = AIChat()
    q = ""
    q = input("こんにちは。御用はなんですか？\n")
    chatai.response(q)
