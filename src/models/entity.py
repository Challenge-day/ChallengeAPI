import enum
from datetime import datetime
from typing import List
from sqlalchemy import String, Enum, Boolean, Integer, DateTime, ForeignKey, func, BigInteger, Float

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    chat_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    lastname: Mapped[str] = mapped_column(String(50), nullable=False)
    points: Mapped[int] = mapped_column(Integer, default=0)
    language_code: Mapped[str] = mapped_column(String(10))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    tasks: Mapped[List["Task"]] = relationship("Task", back_populates="user")
    referrals: Mapped[List["Referral"]] = relationship("Referral", back_populates="referrer", foreign_keys="[Referral.referrer_id]")

    def __init__(self, name, lastname, username, chat_id, language_code='', created_at=None, updated_at=None):
        self.name = name
        self.lastname = lastname
        self.chat_id = chat_id
        self.username = username
        self.language_code = language_code
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
    
    @staticmethod
    def get_user_by_chat_id(session, chat_id):
        return session.query(User).filter_by(chat_id=chat_id).first()
    
class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(50), nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=True)

    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.id'), nullable=False) 
    user: Mapped["User"] = relationship("User", back_populates="tasks")

class Referral(Base):
    __tablename__ = "referrals"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    referrer_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.id'))
    referred_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.id'))

    referrer: Mapped["User"] = relationship("User", foreign_keys=[referrer_id], back_populates="referrals")
    referred: Mapped["User"] = relationship("User", foreign_keys=[referred_id])

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

class Auth(Base):
    __tablename__ = 'auth'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    chat_id: Mapped[int] = mapped_column(BigInteger, nullable=False)

    def __init__(self, username, chat_id):
        self.username = username
        self.chat_id = chat_id

class MiningSession(Base):
    __tablename__ = "mining_session"
    tg_id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    speed: Mapped[float] = mapped_column(Float, default=1.000)
    earned_chl: Mapped[float] = mapped_column(Float, default=0.0)
    last_checked_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

