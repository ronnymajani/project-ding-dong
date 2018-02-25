import time
import esp
from machine import Pin
import constants
import credentials
from networking import NetworkManager
from TelegramBot import TelegramBot

_STATUS_LED = Pin(constants.PIN_LED_STATUS, Pin.OUT)
_ERROR_LED = Pin(constants.PIN_LED_ERROR, Pin.OUT)
_TELEGRAM_BOT = TelegramBot(token = credentials.TOKEN)
_INT_PIN = Pin(constants.INT_PIN, Pin.IN)

def get_telegram_bot():
    return _TELEGRAM_BOT

def get_interrupt_pin():
    return _INT_PIN

def send_telegram_knock_message():
    _TELEGRAM_BOT.sendMessage(credentials.CHANNEL_ID, constants.DOORBELL_MESSAGE)

def send_telegram_knocked_again_message():
    _TELEGRAM_BOT.sendMessage(credentials.CHANNEL_ID, constants.DOORBELL_AGAIN_MESSAGE)

def status_led_on():
    _STATUS_LED.value(1)

def status_led_off():
    _STATUS_LED.value(0)

def error_led_on():
    _ERROR_LED.value(1)

def error_led_off():
    _ERROR_LED.value(0)

def enter_deepsleep(seconds=0):
    if seconds == 0:
        esp.deepsleep()
    else:
        us = seconds * 1000000
        esp.deepsleep(us)

def ERROR_MODE(sleep_time=constants.ERROR_SLEEP_TIME):
    error_led_on()
    status_led_off()
    NetworkManager.disconnect()
    NetworkManager.disable()
    time.sleep(constants.ERROR_PRE_SLEEP_TIME)
    enter_deepsleep(sleep_time)
    while True:
        pass
    
