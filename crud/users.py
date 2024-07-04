from sqlalchemy.orm import Session
from ..users.models.users import Users
from ..users.schemas.users import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(Users).filter(Users.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(Users).filter(Users.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Users).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    # Certificar de hashear a senha corretamente antes de salvar no banco de dados
    fake_hashed_password = (
        user.hashed_password + "not_really_hashed_still"
    )  # Usar um método adequado de hash
    db_user = Users(
        email=user.email, hashed_password=fake_hashed_password, user_name=user.user_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: UserCreate):
    db_user = db.query(Users).filter(Users.id == user_id).first()
    if db_user:
        db_user.email = user.email
        db_user.hashed_password = (
            user.hashed_password + "not_really_hashed_still"
        )  # Usar um método adequado de hash
        db_user.user_name = user.user_name
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(Users).filter(Users.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
