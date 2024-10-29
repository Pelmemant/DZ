from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def f_def() -> dict:
    return {'massage': "Главная страница"}


@app.get("/user/admin")
async def s_def() -> dict:
    return {'massage': "Вы вошли как Админ!"}


@app.get("/user/{user_id}")
async def t_def(user_id: str) -> dict:
    return {'massage': f"Вы вошли как {user_id}"}


@app.get("/user")
async def fo_def(username: str, age: int) -> dict:
    return {'massage': f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
