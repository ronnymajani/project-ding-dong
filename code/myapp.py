from telegram.ext import Updater, CommandHandler
import logging
import time
import credentials

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def start(bot, update):
    update.message.reply_text('Hi! Use /set <seconds> to set a timer')

def main():
    updater = Updater(token=credentials.TOKEN)
    updater.dispatcher.add_error_handler(error)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()

    while True:
        print("Sending message...")
        updater.bot.send_message(credentials.CHANNEL_ID, "Hi")
        time.sleep(5)

    updater.idle()

if __name__ == "__main__":
    main()



logging.getLogger(__name__).info("Done!")
