# main.py
import uvicorn
from fastapi import FastAPI

from db.base import Base, engine
from db.models import User
from db.session import get_db

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/", name="root")
def read_root():
    """
    The read_root function is a view function that returns the root of the API.
    It's purpose is to provide a simple way for users to test if their connection
    to the API is working properly.

    :return: A dictionary
    """
    return {"message": "FastApi is working!"}


# Пример работы с базой данных
def create_user(username, password):
    db = next(get_db())
    new_user = User(username=username, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

if __name__ == '__main__':
    uvicorn.run(app="main:app", reload=True, host="127.0.0.1", port=8000)

    user = create_user('newuser', '123456789')
    print(f"Created new user with ID: {user.id} and username: {user.username}")