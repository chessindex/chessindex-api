import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthcheck")
async def healthcheck():
    return {"message": "Healthcheck OK"}

@app.get("/games")
async def get_games():
    with open("data/games.json", "r") as file:
        games = json.load(file)
    return games