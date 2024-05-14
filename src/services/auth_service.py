from datetime import datetime, timedelta
from pathlib import Path
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    """
    The get_password_hash function takes the password as an argument and returns a hashed version of that password.

    Args: password: str: Password transmitter to hash

    Returns:
    Hashed password
    """
    return pwd_context.hash(password)