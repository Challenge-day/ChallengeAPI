# models/user.py
import enum

from sqlalchemy import String, func
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class UserRole():
    admin = 'admin'
    moderator = 'moderator'
    user = 'user'


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String(100), nullable=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=True)
    last_name: Mapped[str] = mapped_column(String(100), nullable=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    avatar: Mapped[str] = mapped_column(String(255), nullable=True)
    refresh_token: Mapped[str] = mapped_column(String(255), nullable=True)
    banned: Mapped[bool] = mapped_column(default=False)
    confirmed: Mapped[bool] = mapped_column(default=False)
    role: Mapped[str] = mapped_column(default='user')
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())