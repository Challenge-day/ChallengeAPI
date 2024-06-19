# lifespan.py
import logging
import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager
from telegram.ext import Application

from src.start_bot import start_bot

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)
telegram_application: dict[str, Application] = {}

@asynccontextmanager
async def lifespan(_: FastAPI):
    """Init telegram client"""
    application = start_bot()
    telegram_application["application"] = application

    await application.initialize()
    logger.info("Bot initialized")
    
    await application.start()
    logger.info("Telegram client is running.")
    
    yield
    
    await application.stop()
    logger.info("Telegram client is down.")

 