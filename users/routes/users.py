# users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...crud.users import create_user, get_user_by_email, get_users
from ...database.database import SessionLocal
from ...users.schemas.users import UserBase, UserCreate, User

router_users = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router_users.post("/users", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return create_user(db=db, user=user)


@router_users.get("/users", response_model=list[UserBase])
def get_users_endpoint(db: Session = Depends(get_db)):
    users = get_users(db)
    if users:
        return users
    else:
        return []


@router_users.get("/usersteste")
def retornar_teste():
    return "Is running ok"
