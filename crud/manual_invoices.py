from sqlalchemy.orm import Session
from manual_invoices.schemas.manual_invoices import ManualInvoice
from manual_invoices.schemas.manual_invoices import ManualInvoiceCreate


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


def update_manual_invoices(
    db: Session, manualInvoice: ManualInvoice, manual_invoice_id: int
):
    db_manual_invoice = (
        db.query(ManualInvoice)
        .filter(manualInvoice.manual_invoice_id == manual_invoice_id)
        .first()
    )
    if db_manual_invoice:
        db_manual_invoice.invoice_date = manualInvoice.invoice_date
        db_manual_invoice.description = manualInvoice.description
        db_manual_invoice.amount = manualInvoice.amount
        db.commit()
        db.refresh(db_manual_invoice)
    return db_manual_invoice


def delete_manual_invoices(
    db: Session, manualInvoice: ManualInvoice, manual_invoice_id: int
):
    db_manual_invoice = db.query(ManualInvoice).filter(
        manualInvoice.id == manual_invoice_id
    )
    db.delete(db_manual_invoice)
    db.commit()
    db.refresh(db_manual_invoice)
    return db_manual_invoice
