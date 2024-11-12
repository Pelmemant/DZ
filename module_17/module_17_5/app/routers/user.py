from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models.user import User
from app.models.task import Task
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/user', tags=["user"])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    all_u = db.scalars(select(User)).all()
    return all_u


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    us_id = db.scalars(select(User).where(User.id == user_id))
    if us_id is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= 'User was not found'
        )
    else:
        return us_id


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], cre_us: CreateUser):
    db.execute(insert(User).values(username = cre_us.username,
                                     firstname = cre_us.firstname,
                                     lastname = cre_us.lastname,
                                     age = cre_us.age,
                                     slug=slugify(cre_us.username)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'}

@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], up_us: UpdateUser, us_id: int):
    us_id = db.scalars(select(User).where(User.id == us_id))
    if us_id is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    db.execute(update(User).where(User.id == us_id).values(username=up_us.username,
                                   firstname=up_us.firstname,
                                   lastname=up_us.lastname,
                                   age=up_us.age,
                                    slug=slugify(up_us.username)))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Successful'}


@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], us_id: int):
    us_id = db.scalars(select(User).where(User.id == us_id))
    if us_id is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    db.execute(delete(User).where(User.id == us_id))
    db.execute(delete(Task).where(Task.user_id == us_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Successful'}

@router.get('/user_id/tasks')
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)],us_id: int):
    tasks = list(db.scalars(select(Task).where(Task.user_id == us_id)))
    return tasks
