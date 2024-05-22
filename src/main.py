from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def greet():
    return {"hi": "there"}


@app.get("/hmm")
def hmm():
    return {"hmm": "docker"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
