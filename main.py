from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil

app = FastAPI()

@app.get("/")
def message():
    return {"message": "Hello, World!"}