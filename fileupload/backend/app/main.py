from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import os
import uuid
import shutil
import glob

app = FastAPI()

# Set all CORS enabled origins

BACKEND_CORS_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:5500"]

if BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin) for origin in BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.on_event("startup")
async def startup_event():
    if not os.path.exists("/app/out"):
        os.mkdir("/app/out")

    if not os.path.exists("/app/tmp"):
        os.mkdir("/app/tmp")


@app.post("/images")
def file_upload_reservation():
    _id = uuid.uuid4().hex
    retry = 1
    # file exist check
    while os.path.exists(f"/app/tmp/{_id}"):
        _id = uuid.uuid4().hex

        if retry == 5:
            return {"error": {"message": "please retry"}}

        retry += 1

    os.mkdir(f"/app/tmp/{_id}")

    return {"id": _id}


@app.post("/images/{file_id}")
async def file_split_upload(file_id: str,
                            filename: str = Form(),
                            hash: str = Form(),
                            chunk: UploadFile = File()):

    if chunk:
        with open(f"/app/tmp/{file_id}/tmp_data-{hash.zfill(4)}", "wb") as f:
            shutil.copyfileobj(chunk.file, f)


@app.post("/images/{file_id}/merge")
async def file_merge(file_id: str):
    files = glob.glob(f"/app/tmp/{file_id}/*")

    if files:
        with open(f"/app/out/{file_id}.jpg", 'wb') as fout:
            for file in files:
                with open(file, 'rb') as fin:
                    fout.write(fin.read())

    if os.path.exists(f"/app/tmp/{file_id}"):
        shutil.rmtree(f"/app/tmp/{file_id}")

    return {"size": os.path.getsize(f"/app/out/{file_id}.jpg")}


@app.delete("/images/{file_id}")
async def file_delete(file_id: str):

    if os.path.isfile(f"/app/out/{file_id}.jpg"):
        os.remove(f"/app/out/{file_id}.jpg")
    return
