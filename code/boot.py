# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
#import webrepl
#webrepl.start()
gc.collect()

import constants
import esp
from machine import Pin
# Check if the device was woken up by the doorbell or due to a timeout
# If the device didn't wake up due to an interrupt, then go back to sleep
if Pin(constants.INT_PIN, Pin.IN).value() == 0:
    print("[info] woke up due to timeout. going back to sleep")
    esp.deepsleep()

from networking import NetworkManager
NetworkManager.init()
