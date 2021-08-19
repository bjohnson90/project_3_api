import os
import pickle
import sklearn
from typing import Optional

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("./model/random_forest_model.p", "rb") as f:

    model = pickle.load(f)

print("Up and running")

@app.get("/")
def read_root_healthcheck():
    try:
        return {"Health": "OK"}
    except:
        return {"Health": "DEAD"}

# model/.85/20/1.9/-1.2/7 = 1
# model/.65/20/.9/-1.2/5 = 0
@app.get("/model/{twisty}/{cuddly}/{pushy}/{greasy}/{zappy}")
def read_item(twisty: float, cuddly: float, pushy: float, greasy: float, zappy: float):
    prediction = model.predict([[twisty,cuddly,pushy,zappy,greasy]]).tolist()[0]
    return {"prediction": prediction}
