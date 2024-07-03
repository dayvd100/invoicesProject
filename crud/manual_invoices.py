from sqlalchemy.orm import Session
from models.manual_invoices import ManualInvoice
from schemas.manual_invoices import ManualInvoiceCreate


def get_manual_invoices(db: Session, skip: int = 0, limit=100):
    return db.query(ManualInvoice).offset(skip).limit(limit).all()


def create_manual_invoices(db: Session, manualInvoice: ManualInvoiceCreate):
    db_manual_invoice = ManualInvoice(
        invoice_date=manualInvoice.invoice_date,
        description=manualInvoice.description,
        invoice_amount=manualInvoice.invoice_amount,
    )

    db.add(db_manual_invoice)
    db.commit()
    db.refresh()
    return db_manual_invoice
