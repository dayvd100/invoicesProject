from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...crud.users import create_user, get_user_by_email, get_users
from ...database.database import SessionLocal
from ...users.schemas.users import UserBase, UserCreate, User as UserSchema
from ...users.models.users import Users as UserModel

router_users = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router_users.post("/users", response_model=UserSchema)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router_users.get("/users", response_model=list[UserBase])
def get_users_endpoint(db: Session = Depends(get_db)):
    users = get_users(db)
    return users if users else []


@router_users.get("/users/{id}", response_model=UserSchema)
def get_user_endpoint(id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if user:
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"There is no user with the id {id}",
        )


@router_users.delete("/users/{id}", response_model=UserSchema)
def remove_users_endpoint(id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"There is no user with the id {id}",
        )
    db.delete(user)
    db.commit()
    return user
