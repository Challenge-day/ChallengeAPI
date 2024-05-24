import enum
from datetime import datetime
from sqlalchemy import String, Enum, Boolean, Integer, DateTime, BigInteger, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Role(enum.Enum):
    admin: str = "admin"
    moderator: str = "moderator"
    user: str = "user"

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(50))
    language_code: Mapped[str] = mapped_column(String(10))

    role: Mapped[Role] = mapped_column(
        Enum(Role), default=Role.user, nullable=True
    )

    confirmed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=True)

    messages: Mapped[list["Message"]] = relationship("Message", back_populates="user")

class Message(Base):
    __tablename__ = 'messages'
    id: Mapped[int] = mapped_column(primary_key=True)
    message_id: Mapped[int] = mapped_column(Integer, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    chat_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    text: Mapped[str] = mapped_column(String(4096), nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    command: Mapped[str] = mapped_column(String(255), nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="messages")