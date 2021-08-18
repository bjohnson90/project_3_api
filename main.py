from typing import Optional
import uvicorn
from fastapi import FastAPI

app = FastAPI()
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

if __name__ == '__main__':

    uvicorn.run(app, host='127.0.0.1', port=4000, debug=True)