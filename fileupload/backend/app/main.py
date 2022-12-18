from fastapi import FastAPI, File, UploadFile

import os

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": 0}


@app.post("/")
async def file_split_upload(file: bytes = File()):
    if not os.path.exists("/app/out"):  # ディレクトリが存在しないなら
        os.mkdir("/app/out")  # 作成
    """
    pathをバイナリファイルとして開きdataを書き込む
    """
    with open("/app/out/data", 'ab') as fout:
        fout.write(file)
    return {"file_size": len(file)}
