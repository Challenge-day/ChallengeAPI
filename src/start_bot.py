# start_bot.py
import logging

from telegram.ext import Application

from src.db.config import settings
from src.db.connect import engine
from src.models.entity import Base

# Tables are created here
Base.metadata.create_all(engine)

TOKEN = settings.TELEGRAM_TOKEN

def start_bot():
    application = Application.builder().token(TOKEN).read_timeout(7).get_updates_read_timeout(42).build()
    return application
    

   