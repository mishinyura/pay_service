from sqlalchemy import Column, Integer, String, ForeignKey
from app.db import Base
from app.models.base_model import BaseModel

class Company(Base, BaseModel):
    __tablename__ = 'companies'

    name = Column(String)
    company_id = Column(Integer, primaty_key=True, autoincrement=True)