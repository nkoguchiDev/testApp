import requests

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
