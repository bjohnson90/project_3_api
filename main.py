from typing import Optional
import uvicorn
from fastapi import FastAPI
import os

if os.environ.get('PORT',None):
    port = int(os.environ['PORT'])
else:
    port=None

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

if port:
    uvicorn.run(app,port=port)
else:
    uvicorn.run(app, host='127.0.0.1', port=8080, debug=True)