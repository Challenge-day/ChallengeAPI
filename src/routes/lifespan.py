# lifespan.py
import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from start_bot import start_bot

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Init telegram client"""
    logger.info("Starting bot...")
    on_startup, on_shutdown = await start_bot()
    await on_startup()
    logger.info("Bot started.")
    yield
    logger.info("Shutting down bot...")
    await on_shutdown()
    logger.info("Bot shut down.")