from telegram import Update
from telegram.ext import ContextTypes
from src.db.connect import DBSession

from src.models.entity import User

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with DBSession() as session:
        try: # Check if user doesnt exist create user
             with session.begin():
                 chat_id = update.message.chat_id
                 user = User.get_user_by_chat_id(session, chat_id)
                 if not user:
                    user = update.effective_user
                    new_user = User(name=user.name, lastname=user.last_name, username=user.username,
                                    chat_id=user.id)
                    session.add(new_user)
                    session.commit()
                    context.user_data['user'] = user
                    await update.message.reply_text(f"Dear {user.name} you are registered successfully.")
        except Exception as er:
            session.rollback()
            await update.message.reply_text(f"An error occurred: {er}")

            
            
