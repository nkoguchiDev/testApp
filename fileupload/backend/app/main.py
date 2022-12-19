from fastapi import FastAPI, File, UploadFile

import os
import uuid
import pathlib

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    if not os.path.exists("/app/out"):  # ディレクトリが存在しないなら
        os.mkdir("/app/out")  # 作成


@app.post("/images")
def file_upload_reservation():
    _id = uuid.uuid4().hex
    retry = 1
    # file exist check
    while os.path.isfile(f"/app/out/{_id}.jpg"):
        _id = uuid.uuid4().hex

        if retry == 5:
            return {"error": {"message": "please retry"}}

        retry += 1

    file = pathlib.Path(f"/app/out/{_id}.jpg")
    file.touch()
    return {"id": _id}


@app.post("/images/{file_id}")
async def file_split_upload(file_id: str, file: bytes = File()):

    with open(f"/app/out/{file_id}.jpg", "ab") as f2:
        f2.write(file)

    current_size = os.path.getsize(f"/app/out/{file_id}.jpg")

    return {"id": file_id, "current_size": current_size}


@app.delete("/images/{file_id}")
async def file_delete(file_id: str):
    if os.path.isfile(f"/app/out/{file_id}.jpg"):
        os.remove(f"/app/out/{file_id}.jpg")

    return
