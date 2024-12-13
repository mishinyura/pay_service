from sqlalchemy import Column, Integer, String, UUID, Numeric, ForeignKey

from app.db import Base
from app.models.base_model import BaseModel


class Payments(BaseModel, Base):
    __table__ = "payments"

    user_id = Column(UUID(as_uuid=True), nullable=False)
    payments_id = Column(String, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    email = Column(String)
    type = Column(String(30), nullable=False)
    abc_test = Column(String(30), nullable=False)
    payments_status = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey('companies.company_id'), nullable=False)

    def __repr__(self):
        return (
            f"Payment(user_id{self.user_id}),"
            f"payment_id={self.payments_id},"
            f"amount={self.amount},"
            f"email={self.email},"
            f"type={self.type},"
            f"payments_status={self.payments_status}"
        )

    def __str__(self):
        return (
            f"Payment(user_id{self.user_id}),"
            f"payment_id={self.payments_id},"
            f"amount={self.amount},"
            f"email={self.email},"
            f"type={self.type},"
            f"payments_status={self.payments_status}"
        )
