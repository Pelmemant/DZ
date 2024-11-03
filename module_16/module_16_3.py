from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def u_get() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def u_post(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                 age: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]) -> str:
    new_in = str(int(max(users, key=int))+1)
    users[new_in] = f"Имя {username}, возраст {age}"
    return "Юзер создан"

@app.put("/user/{user_id}/{username}/{age}")
async def u_put(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')], username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                 age: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]) -> str:
    users[user_id] = f"Имя {username}, возраст {age}"
    return "Юзер обновлён"

@app.delete("/user/{user_id}")
async def u_del(user_id: Annotated[str, Path(ge=1, le=100, description='Enter User ID', example='1')]) -> str:
    users.pop(user_id)
    return "Юзер удалён"
