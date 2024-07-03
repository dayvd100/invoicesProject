from pydantic import BaseModel
from datetime import date


class ManualInvoiceBase(BaseModel):
    invoice_date: date
    description: str
    invoice_amount: float


class ManualInvoiceCreate(ManualInvoiceBase):
    owner_id: int


class ManualInvoice(ManualInvoiceBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
