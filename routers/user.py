from typing import List

from fastapi import APIRouter, Depends, HTTPException

from ..config import get_database_connection
from ..database import create_user, get_user, get_users, update_user, delete_user
from ..schemas import User, UserCreate

router = APIRouter()


@router.post("/")
def create(user: UserCreate, db=Depends(get_database_connection)):
    cursor = db.cursor()
    create_user(cursor, user)
    db.commit()
    return {"message": "User created."}


@router.get("/", response_model=List[User])
def read_all(db=Depends(get_database_connection)):
    cursor = db.cursor(dictionary=True)
    users = get_users(cursor)
    return users


@router.get("/{user_id}", response_model=User)
def read(user_id: int, db=Depends(get_database_connection)):
    cursor = db.cursor(dictionary=True)
    user = get_user(cursor, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}")
def update(user_id: int, user: UserCreate, db=Depends(get_database_connection)):
    cursor = db.cursor()
    update_user(cursor, user_id, user)
    db.commit()
    return {"message": "User updated."}


@router.delete("/{user_id}")
def delete(user_id: int, db=Depends(get_database_connection)):
    cursor = db.cursor()
    delete_user(cursor, user_id)
    db.commit()
    return {"message": "User deleted"}
