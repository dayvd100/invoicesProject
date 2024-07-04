from sqlalchemy import Column, Float, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from database.database import Base


class ManualInvoice(Base):
    __tablename__ = "manualinvoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_date = Column(Date)
    description = Column(String)
    invoice_amount = Column(Float)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="manual_invoices")
