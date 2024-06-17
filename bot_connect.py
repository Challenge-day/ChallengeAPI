import logging
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler


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

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()



if __name__ == "__main__":
    main()