import logging
import asyncio
from telegram.ext import Application, CommandHandler

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

    async def on_startup(app):
        await app.initialize()
        await app.start()

    async def on_shutdown(app):
        await app.stop()
    
    await on_startup(application)
    try:
        await asyncio.sleep(60) 
            
    except asyncio.CancelledError:
        await on_shutdown(application)
