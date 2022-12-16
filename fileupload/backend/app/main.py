from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": 0}

@app.post("/")
async def file_split_upload(file:bytes=File()):
    filename = fields.filename[0];
    hash = fields.hash[0];
    chunk = files.chunk[0];
    dir = `${STATIC_TEMPORARY}/${filename}`;