# start_bot.py
import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from src.db.config import settings
from src.db.connect import engine
from src.models.entity import Base
from src.repositories.users import start

# Tables are created here
Base.metadata.create_all(engine)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = settings.TELEGRAM_TOKEN

async def start_bot():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    # application.run_polling()

    await application.initialize()
    logger.info("Telegram client initialized.")

    async def on_startup():
        logger.info("Starting Telegram client...")
        # await application.start()
        application.add_handler(CommandHandler("start", start))
        logger.info("Telegram client is running.")

    async def on_shutdown():
        logger.info("Stopping Telegram client...")
        await application.stop()
        await application.shutdown()
        logger.info("Telegram client is down.")

    return on_startup, on_shutdown
