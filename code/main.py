# TODO: after wake up and first message sent, go into light sleep for 10 seconds,
# if the doorbell is rung again, send another message, and reset 10 second counter
# if 10 seconds has passed then go into deep sleep
# TODO: interrupt causes message to be sent

import time
import constants
import credentials
from networking import NetworkManager
from TelegramBot import TelegramBot


def test():
    from machine import Pin
    x = Pin(14, Pin.IN)
    v = x.value()
    while True:
        print("X:%d, V:%d"%(x.value(), v))
        time.sleep(1)



def setup():
    # connect to wifi
    NetworkManager.connect(credentials.WIFI_SSID, credentials.WIFI_PASS, timeout=5)


def main():
    bot = TelegramBot(token = credentials.TOKEN)
    print("Sending message...")
    bot.sendMessage(credentials.CHANNEL_ID, constants.DOORBELL_MESSAGE)


# Run main function
if __name__ == "__main__":
    # test()
    setup()
    main()

