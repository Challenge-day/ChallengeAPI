# lifespan.py
import logging
import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.start_bot import start_bot

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Init telegram client"""
    application = await start_bot()
    await application.initialize()
    logger.info("Bot initialized")
    
    bot_task = asyncio.create_task(application.start())
    # await application.start()
    # application.run_polling()
    logger.info("Bot started")
    
    yield
    
    # await application.stop()
    await bot_task.cancel()
    await application.stop_running()
    logger.info("Bot shut down")