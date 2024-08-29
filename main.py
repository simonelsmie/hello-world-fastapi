from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/")
async def hello() -> dict:
    return {"message": "Hello World"}


@app.get("/healthz")
async def healthz() -> dict:
    return {"message": "OK"}
