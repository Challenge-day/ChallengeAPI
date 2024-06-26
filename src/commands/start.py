import logging
from aiogram import types

from src.db.connect import DBSession
from src.models.entity import User, Auth

logger = logging.getLogger(__name__)

async def start_command(message: types.Message) -> None:
    logger.info("Received /start command")
    with DBSession() as session:
        try: # Check if user doesn't exist create user
             with session.begin():
                 tg_id = message.chat.id
                 user = User.get_user_by_chat_id(session, tg_id)

                 if not user:
                     user_info = message.from_user
                     new_user = User(name=user_info.first_name, 
                                    lastname=user_info.last_name, 
                                    username=user_info.username,
                                    tg_id=user_info.id
                                    )
                     session.add(new_user)
                     session.flush()

                    # Create an Auth entry for the new user
                     new_auth = Auth(
                         username=user_info.username or "",
                         tg_id=user_info.id
                     )

                     session.add(new_auth)
                     session.commit()

                     await message.answer(f"Dear {user_info.first_name} you are registered successfully.")
                 else:
                     await message.answer(f"Welcome back, {user.name}!")
        
        except Exception as er:
            session.rollback()
            logger.error("Error occurred: %s", er)
            await message.answer(f"An error occurred: {er}")
   
            
