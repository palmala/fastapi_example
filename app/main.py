import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    return {"status": "ok", "result": str(num1 + num2)}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
