from fastapi import FastAPI

app = FastAPI()

counter = 0

@app.get("/api/python")
def hello_world():
    counter += 1
    return {"api calls": counter}
