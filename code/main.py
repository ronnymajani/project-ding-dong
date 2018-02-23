# TODO: interrupt causes message to be sent
# TODO: sleep, and wakeup with interrupts

from TelegramBot import TelegramBot
import time
import credentials
from networking import NetworkManager


def setup():
    # connect to wifi
    NetworkManager.connect(credentials.WIFI_SSID, credentials.WIFI_PASS)


def main():
    print("Life")
    bot = TelegramBot(token = credentials.TOKEN)
    while True:
        print("Sending message...")
        bot.sendMessage(credentials.CHANNEL_ID, "Hi")
        time.sleep(5)



# Run main function
if __name__ == "__main__":
    setup()
    main()

