import ray

from gen import AIChat
from gen import split_message, generate_voice


def main():
    # AIChat のインスタンスを作成する
    chatai = AIChat()

    # 利用者から質問を受け取る
    # クラスか関数化しても良いかも
    q = ""
    q = input("こんにちは。御用はなんですか？\n")

    # 返答を受け取る
    text = chatai.talk(q)

    # 下記の処理を非同期で並列処理する
    # -> rayを使用して分散並列処理を行う
    voice_list = iter(split_message(text))

    if len(voice_list) % 2 != 0:
        generate_voice(voice_list[0])
        del voice_list[0]
    ray.init(num_cpus=2)
    for i, j in zip(voice_list, voice_list):
        generate_voice.remote(i), generate_voice.remote(j)


if __name__ == "__main__":
    main()
