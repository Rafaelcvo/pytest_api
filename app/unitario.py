from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_hello():
    return {"message": "Hello World"}