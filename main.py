from fastapi import FastAPI
from dotenv import load_dotenv
from routers.upload import router as upload_router

load_dotenv()
app = FastAPI()
app.include_router(upload_router)

@app.get("/")
def message():
    return {"message": "Hello, World!"}
