from pydantic import BaseModel
from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List


app = FastAPI()

users = []
class User(BaseModel):
    id: int = None
    name: str
    age: int


@app.get("/")
async def u_get() -> List[User]:
    return users

@app.post("/user/{username}/{age}'")
async def u_post(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                 age: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]) -> str:
    new_user = User(id = len(users) + 1, name = username, age =  age)
    users.append(new_user)
    return "Юзер создан"

@app.put("/user/{user_id}/{username}/{age}")
async def u_put(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')], username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                 age: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]) -> str:
    try:
        users[user_id] = f"Имя {username}, возраст {age}"
        return "Юзер обновлён"
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


@app.delete("/user/{user_id}")
async def u_del(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]) -> str:
    try:
        users.pop(user_id)
        return "Юзер удалён"
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')