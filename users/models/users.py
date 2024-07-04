from sqlalchemy import Column, Integer, String

# from sqlalchemy.orm import relationship
from ...database.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    # manual_invoices = relationship("ManualInvoice", back_populates="owner")
