import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import settings
logging.basicConfig(filename="bot.log", level=logging.INFO)

async def greet_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Вызван /start")
    await update.message.reply_text("Шо ты, голова?")


async def talk_to_me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    print(text)
    await update.message.reply_text(text)

def main():
    application = Application.builder().token(settings.API_KEY).build()
    application.add_handler(CommandHandler("start", greet_user))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, talk_to_me))
    logging.info("Бот пошел, родной!")
    application.run_polling()

if __name__ == '__main__':
    main()
 