from fastapi import FastAPI

app = FastAPI()

global counter
counter = 0

@app.get("/api/python")
def hello_world():
    counter += 1
    return {"api calls": counter}
