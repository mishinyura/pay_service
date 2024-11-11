from pydantic import BaseModel
from typing import Optional

# Модель товара
class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    email: str