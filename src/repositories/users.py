from sqlalchemy.orm import Session
from src.models.entity import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id: int) -> User:
        return self.session.query(User).filter(User.id == user_id).first()

    def get_by_telegram_id(self, telegram_id: int) -> User:
        return self.session.query(User).filter(User.telegram_id == telegram_id).first()
    
    def get_by_email(self, email: str) -> User:
        return self.session.query(User).filter(User.email == email).first()

    def add(self, user: User):
        self.session.add(user)
        self.session.commit()

    def update(self, user: User):
        self.session.merge(user)
        self.session.commit()

    def delete(self, user: User):
        self.session.delete(user)
        self.session.commit()

    def validate_user(self, email: str, password: str) -> bool:
        user = self.get_by_email(email)
        if user and user.password == password:
            return True
        return False
