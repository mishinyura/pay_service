from fastapi import FastAPI, HTTPException
from models import Product, User

app = FastAPI()


# Хранилище товаров и пользователей
products = []
users = []

# Эндпоинты для работы с товарами

@app.post("/products/", response_model=Product)
def create_product(product: Product):
    products.append(product)
    return product

@app.get("/products/", response_model=list[Product])
def get_products():
    return products

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            del products[index]
            return {"detail": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")

# Эндпоинты для работы с пользователями

@app.post("/users/", response_model=User)
def create_user(user: User):
    users.append(user)
    return user

@app.get("/users/", response_model=list[User])
def get_users():
    return users

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            del users[index]
            return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

# Запуск приложения
# Для запуска приложения используйте команду: uvicorn filename:app --reload