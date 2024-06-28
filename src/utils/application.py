# lifespan.py
import logging
from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from contextlib import asynccontextmanager

from src.db.config import settings
from src.models.entity import Base
from src.db.connect import engine
from src.commands.start import start_command
from src.commands.restart import restart_command
from src.commands.stop import stop_command

# Tables are created here
Base.metadata.create_all(engine)

TOKEN = settings.TELEGRAM_TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@asynccontextmanager
async def lifespan(_: FastAPI):
    """Init telegram client"""

    await dp.start_polling(bot)
    logger.info("Telegram client is running.")
        
    yield
 
    await dp.stop_polling()
    logger.info("Telegram client is down.")
       
dp.message.register(start_command, Command(commands=["start"]))
dp.message.register(stop_command, Command(commands=["stop"]))
dp.message.register(restart_command, Command(commands=["restart"]))



    


 