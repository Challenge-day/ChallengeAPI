
from sqlalchemy.orm import Session

from models.user import User
from schemas.user import UserRegisterModel

def update_user(user: User, session: Session):
    """
        Function update_user user and session to work with the database
        Args:
        user: User: user's object
        session: Session: Pass a function session object
        Returns:
        Updated user object
    """
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def create_user(body: UserRegisterModel, session: Session):
    """
    The create_user function creates a new user in the database

    Args:
    email: str: We specify the email and password in the body of the request of the user we want to create
    session: Session: Pass a function session object

    Returns:
    User class object we created in the database
    """
    is_db_full = session.query(User).first()
    
    
    # TODO hashed_password = get_password_hash(password=body.password)
    user = User(email=body.email,
                # password=hashed_password,
                username=body.username,
                )
    user.first_name = None if body.first_name == "string" else body.first_name
    user.last_name = None if body.last_name == "string" else body.last_name
    user.username = None if body.username == "string" else body.username
    
    if not is_db_full:
        user.role = 'admin'
    user = update_user(user, session)
    return user