# from telegram.ext import Updater, CommandHandler

from TelegramBot import TelegramBot
import time
import credentials



def main():
    bot = TelegramBot(token = credentials.TOKEN)
    while True:
        print("Sending message...")
        bot.sendMessage(credentials.CHANNEL_ID, "Hi")
        time.sleep(5)



# Run main function
if __name__ == "__main__":
    main()

