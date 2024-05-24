from sqlalchemy.orm import Session
from src.models.entity import Message

class MessageRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, message_id: int) -> Message:
        return self.session.query(Message).filter(Message.id == message_id).first()

    def get_by_user_id(self, user_id: int) -> list[Message]:
        return self.session.query(Message).filter(Message.user_id == user_id).all()

    def add(self, message: Message):
        self.session.add(message)
        self.session.commit()

    def update(self, message: Message):
        self.session.merge(message)
        self.session.commit()

    def delete(self, message: Message):
        self.session.delete(message)
        self.session.commit()
