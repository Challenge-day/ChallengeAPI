from datetime import datetime, timedelta
from pathlib import Path
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    """
    Функція get_password_hash приймає пароль як аргумент і повертає хешовану версію цього пароля.

    Args: password: str: Передавача пароля, який потрібно хешувати

    Returns:
    Хешований пароль
    """
    return pwd_context.hash(password)