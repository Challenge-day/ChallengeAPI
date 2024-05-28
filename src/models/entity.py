import enum
from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, Enum, Boolean, Integer, DateTime, BigInteger, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
class Role(enum.Enum):
    admin: str = "admin"
    moderator: str = "moderator"
    user: str = "user"

class User(Base):
    __tablename__ = 'users'
    tg_id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    tasks: Mapped[List["Task"]] = relationship("Task", back_populates="user")
    points: Mapped[int] = mapped_column(Integer, default=0)
    messages: Mapped[list["Message"]] = relationship("Message", back_populates="user")
    language_code: Mapped[str] = mapped_column(String(10))
    role: Mapped[Role] = mapped_column(Enum(Role), default=Role.user, nullable=True)
    referrals: Mapped[List["Referral"]] = relationship("Referral", back_populates="referrer")
    
    def update_username(self, new_username: str):
        if self.username != new_username:
            self.username = new_username

class Task(Base):
    __tablename__ = "tasks"
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(50), nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False) 
    user: Mapped[User] = relationship("User", back_populates="tasks")

class Referral(Base):
    __tablename__ = "referrals"
    referrer_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    referred_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    referrer: Mapped["User"] = relationship("User", foreign_keys=[referrer_id], back_populates="referrals")
    referred: Mapped["User"] = relationship("User", foreign_keys=[referred_id])
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

class Message(Base):
    __tablename__ = 'messages'
    message_id: Mapped[int] = mapped_column(Integer, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    chat_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    text: Mapped[str] = mapped_column(String(4096), nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    command: Mapped[str] = mapped_column(String(255), nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="messages")