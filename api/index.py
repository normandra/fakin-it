from fastapi import FastAPI

app = FastAPI()
state = {}
state["counter"] = 0

@app.get("/api/python")
def hello_world():
    state["counter"] += 1
    return {"api calls": state["counter"]}
