# main.py
import uvicorn
from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import FastAPI, Depends, HTTPException, status
from typing import List

from src.db.connect import get_db
from src.models.entity import Base, User, Message
from src.repositories.users import UserRepository
from src.repositories.messages import MessageRepository
from src.schemas.schemas import UserCreate, UserLogin, MessageCreate, MessageResponse
from src.routes import referrals

app = FastAPI(swagger_ui_parameters={"operationsSorter": "method"})
app.include_router(referrals.router, prefix="/api", tags=["referrals"])

@app.get("/", name="root")
def read_root():
    """
    The read_root function is a view function that returns the root of the API.
    It's purpose is to provide a simple way for users to test if their connection
    to the API is working properly.

    :return: A dictionary
    """
    return {"message": "FastApi is working!"}

@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    """
    The healthchecker function is a simple function that checks if the database
    is configured correctly. It does this by executing a simple SQL query and checking
    if it returns any results. If it doesn't, then we know something is wrong with the 
    database configuration.
    
    :param db: Session: Pass the database connection to the function
    :return: A dictionary with a message key
    """
    try:
        result = db.execute(text("SELECT 1")).fetchone()
        print(result)
        if result is None:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Database is not configured correctly")
        return {"message": "Database successfully connected"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Error connecting to the database")
    

@app.post("/users/", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    db_user = user_repo.get_by_telegram_id(user.telegram_id)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    
    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
        telegram_id=user.telegram_id,
        first_name=user.first_name,
        language_code=user.language_code
    )

    user_repo.add(new_user)
    return new_user

@app.post("/login/")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    if user_repo.validate_user(user.email, user.password):
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
@app.post("/messages/", response_model=MessageResponse)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    message_repo = MessageRepository(db)
    new_message = Message(
        message_id=message.message_id,
        user_id=message.user_id,
        chat_id=message.chat_id,
        text=message.text,
        command=message.command
    )
    message_repo.add(new_message)
    return new_message

@app.get("/messages/{user_id}", response_model=List[MessageResponse])
def read_messages(user_id: int, db: Session = Depends(get_db)):
    message_repo = MessageRepository(db)
    messages = message_repo.get_by_user_id(user_id)
    return messages

if __name__ == '__main__':
    uvicorn.run(app="main:app", reload=True, host="127.0.0.1", port=8000)
   
