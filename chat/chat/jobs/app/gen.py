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
        self.message = "ME:これより先は語尾を「のだ」または「なのだ」にしてください。\nAI:了解なのだ。よろしくなのだ"

    def response(self, user_input):
        # openai の GPT-3 モデルを使って、応答を生成する
        self.message = f"{self.message}\nME:{user_input}"
        print(self.message)
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=self.message,
            max_tokens=100,
            temperature=0.7,  # 生成する応答の多様性
            frequency_penalty=0.2,
            presence_penalty=0,
        )
        response = response['choices'][0]['text'].replace("\n", "")
        # 応答のテキスト部分を取り出して返す
        return response


if __name__ == "__main__":
    # AIChat のインスタンスを作成する
    chatai = AIChat()
    print(chatai.response("あなたの名前は何ですか？"))
