from typing import List
from pydantic import BaseModel, EmailStr
from manual_invoices.schemas import ManualInvoice


class UserBase(BaseModel):
    user_name: str
    email: EmailStr


class UserCreate(UserBase):
    hashed_password: str


class User(UserBase):
    id: int
    manual_invoices: List[ManualInvoice] = []

    class Config:
        orm_mode = True
