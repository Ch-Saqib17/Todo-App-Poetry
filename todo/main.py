from fastapi import FastAPI

app : FastAPI = FastAPI(title="Todo App")

@app.get("/")
def index():
    return {"message": "Hello World"}