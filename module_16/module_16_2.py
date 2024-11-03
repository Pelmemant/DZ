from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()


@app.get("/")
async def f_def() -> dict:
    return {'massage': "Главная страница"}


@app.get("/user/admin")
async def s_def() -> dict:
    return {'massage': "Вы вошли как Админ!"}


@app.get("/user/{user_id}")
async def t_def(user_id: int = Path(ge=1, le=100, description='Enter User ID', example='1')) -> dict:
    return {'massage': f"Вы вошли как {user_id}"}


@app.get("/user/{username}/{age}")
async def fo_def(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                 age: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]) -> dict:
    return {'massage': f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
