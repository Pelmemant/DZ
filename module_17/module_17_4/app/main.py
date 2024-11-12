from fastapi import FastAPI
from routers import task, user


app = FastAPI()

@app.get("/")
async def m_main() -> dict:
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)
