import requests
import openai
import os
import re
import ray

from config import settings


def generate_voice(text: str, file_name: str):
    query = requests.post(
        url=settings.voice_query_endpoint,
        params={"speaker": 1, "text": text})

    voice_wav = requests.post(
        url=settings.voice_generator_endpoint,
        params={"speaker": 1},
        json=query.json(),
        headers={"Content-Type": "application/json"})

    if not os.path.exists(f"{settings.app_base_dir}/voice"):
        os.makedirs(f"{settings.app_base_dir}/voice")
    with open(f"{settings.app_base_dir}/voice/{file_name}.wav", "wb") as f:
        f.write(voice_wav.content)


def split_message(messages: str) -> list:
    # 日本語文を一言ごとに分割する
    return re.split(r"(?<=[。|、|\!|\?])", messages)


def post_message_to_GTP(prompt: str) -> str:
    # openai の GPT-3 モデルを使って、応答を生成する
    created_message = openai.Completion.create(
        engine=settings.gpt_ai_engine,
        prompt=prompt,
        max_tokens=1000,
        temperature=0.7,  # 生成する応答の多様性
        frequency_penalty=0.2,
        presence_penalty=0,
    )

    return "".join([choice.get("text", "")
                   for choice in created_message.choices])


def get_learning_data() -> str:
    learning_data = ""
    with open(f"{settings.app_base_dir}/history.txt", 'r') as f:
        learning_data = f.read()
    return learning_data


class AIChat:
    def __init__(self):
        # ※冒頭で作成したopenai の APIキーを設定してください
        openai.api_key = settings.gpt_api_key
        self.message = get_learning_data()

    def learn(self, user_input):
        prompt = f"{self.message}\nME:{user_input}"

        texts = post_message_to_GTP(prompt=prompt)

        with open(f"{settings.app_base_dir}/history.txt", 'w') as f:
            f.write(prompt)
            f.write(texts)

    def talk(self, user_input: str):
        prompt = f"{self.message}\nME:{user_input}"

        texts = post_message_to_GTP(prompt=prompt)

        return texts.replace(f"{settings.chara_name}:", "")


if __name__ == "__main__":
    # AIChat のインスタンスを作成する
    chatai = AIChat()
    q = ""
    q = input("こんにちは。御用はなんですか？\n")
    text = chatai.talk(q)
    print(text)
    voice_gen_list = split_message(text)
    # 下記の処理を非同期で並列処理する
    # -> rayを使用して分散並列処理を行う
    for i in voice_gen_list:
        ray.init(num_cpus=4)
        generate_voice(text)
