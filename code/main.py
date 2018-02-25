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

def wait_for_another_knock():
    """Keeps checking for the doorbell to be rung again.
    If after 10 seconds it hasn't been rung, we continue (and go back into deep sleep)"""
    t = 0
    while t < 10:
        time.sleep(1)
        if get_interrupt_pin().value() == 1:
            t = 0
            send_telegram_knocked_again_message()
        else:
            t += 1

def main():
    status_led_on()
    print("Sending message...")
    send_telegram_knock_message()
    wait_for_another_knock()
    status_led_off()
    # TODO: uncomment
    # enter_deepsleep()


# Run main function
if __name__ == "__main__":
    # test()
    setup()
    main()

