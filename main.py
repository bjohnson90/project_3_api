from typing import Optional
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Up and running")

@app.get("/")
def read_root_healthcheck():
    try:
        return {"Health": "OK"}
    except:
        return {"Health": "DEAD"}


@app.get("/model/{twisty}/{cuddly}/{pushy}/{greasy}/{zappy}")
def read_item(twisty: int, cuddly: int, pushy: int, greasy: int, zappy: int):
    # XXX: Use model here
    return {"twisty": twisty, "cuddly": cuddly, "pushy": pushy, "greasy": greasy, "zappy": zappy}
