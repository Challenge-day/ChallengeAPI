# lifespan.py
import logging
import asyncio
from fastapi import FastAPI
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from src.start_bot import start_bot

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    """Init telegram client"""
    application = await start_bot()
    
    await application.start()
    logger.info("Telegram client is running.")
    
    yield
    
    await application.stop()
    logger.info("Telegram client is down.")

 