# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
# Set CPU frequency to minimum possible value 80MHz
import machine
import esp
machine.freq(80000000)
esp.sleep_type(esp.SLEEP_LIGHT)

import constants

# Check if the device was woken up by the doorbell or due to a timeout
# If the device didn't wake up due to an interrupt, then go back to sleep
# TODO: uncomment
# from machine import Pin
# if Pin(constants.INT_PIN, Pin.IN).value() == 0:
#     print("[info] woke up due to timeout. going back to sleep")
#     esp.deepsleep()

import gc
#import webrepl
#webrepl.start()
gc.collect()

from networking import NetworkManager
NetworkManager.init()
