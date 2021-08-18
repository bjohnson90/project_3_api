from typing import Optional

from fastapi import FastAPI

app = FastAPI()


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