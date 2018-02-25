# TODO: implement battery status check

import time
import machine
import constants
import credentials
from helpers import *
from networking import NetworkManager


def test():
    from machine import Pin
    x = Pin(14, Pin.IN)
    v = x.value()
    while True:
        print("X:%d, V:%d"%(x.value(), v))
        time.sleep(1)



def setup():
    status_led_off()
    error_led_off()
    # connect to wifi
    if not NetworkManager.connect(credentials.WIFI_SSID, credentials.WIFI_PASS, timeout=constants.WIFI_TIMEOUT):
        ERROR_MODE()

def main():
    status_led_on()
    print("Sending message...")
    send_telegram_knock_message()
    status_led_off()
    # TODO: uncomment
    # enter_deepsleep()


# Run main function
if __name__ == "__main__":
    # test()
    setup()
    main()

