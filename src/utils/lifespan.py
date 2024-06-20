# lifespan.py
import logging
from fastapi import FastAPI
from telegram.ext import CommandHandler

from contextlib import asynccontextmanager

from src.start_bot import start_bot
from src.repositories.users import start

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)
application = start_bot()

@asynccontextmanager
async def lifespan(_: FastAPI):
    """Init telegram client"""
    
    async with application:
        
        await application.start()
        logger.info("Telegram client is running.")
    
        yield
    
        await application.stop()
        logger.info("Telegram client is down.")
       

application.add_handler(CommandHandler("start", start))
# application.run_polling()
 