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

    def response(self, user_input):
        # openai の GPT-3 モデルを使って、応答を生成する
        response = openai.Completion.create(
            engine="text-davinci-002",  # text-davinci-003 を指定した方がより自然な文章が生成されます
            prompt=user_input,
            max_tokens=1024,
            temperature=0.5,  # 生成する応答の多様性
        )

        # 応答のテキスト部分を取り出して返す
        return response['choices'][0]['text']
