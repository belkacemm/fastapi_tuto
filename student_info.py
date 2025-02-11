from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get():
    return {"message": "Welcome to my api"}

@app.get("/student/{id}")
async def get_student(id: int):
    return {"id": id}