from telegram import Update
from telegram.ext import ContextTypes
from src.db.connect import DBSession

from src.models.entity import User, Auth

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with DBSession() as session:
        try: # Check if user doesnt exist create user
             with session.begin():
                 chat_id = update.message.chat_id
                 user = User.get_user_by_chat_id(session, chat_id)

                 if not user:
                     user_info = update.effective_user
                     new_user = User(name=user_info.name, 
                                    lastname=user_info.last_name, 
                                    username=user_info.username,
                                    chat_id=user_info.id
                                    )
                     session.add(new_user)
                     session.flush()

                    # Create an Auth entry for the new user
                     new_auth = Auth(
                         username=user_info.username or "",
                         chat_id=user_info.id
                     )

                     session.add(new_auth)
                     session.commit()

                     context.user_data['user'] = user_info
                     await update.message.reply_text(f"Dear {user_info.name} you are registered successfully.")
                 else:
                     await update.message.reply_text(f"Welcome back, {user.name}!")
        
        except Exception as er:
            session.rollback()
            await update.message.reply_text(f"An error occurred: {er}")

            
            
