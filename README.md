# Project Ding Dong
An automated doorbell that messages you via a Telegram channel whenever someone rings your doorbell. Powered by the ESP8266
###### [Full Project Description at Hackaday.io](https://hackaday.io/project/61540-project-ding-dong)
------------------------

***The README is not yet complete***

### NOTE:
I omitted a file called `credentials.py` in which I store the TOKEN of my bot and the channel ID that it will push messages to.
So to be able to get the code running don't forget to create this file in the folder `code` and fill it as follows:
``` python
# credentials.py

# This is the generated access token for your telegram bot
TOKEN = ""
# This is the chat id of the channel your bot will push messages to
CHANNEL_ID = ""
# wireless credentials
WIFI_SSID = ""
WIFI_PASS = ""
```


Tools Used:
-------------
- **OpenSCAD** to edit the 3D models for the chassis
- **Telegram** to be able to communicate with the *doorbell*
- **Eagle** to be able to edit the electronic schematics
- **esptool** for flashing the ESP8266
- **mpfshell** for easily transfering files from the computer to the ESP8266

Repository layout:
----------
- **chassis:** this folder contains the OpenSCAD files for the chassis that encompasses the entire system
- **code:** this folder contains the code that will run on the ESP8266
- **schematics:** this folder contains the electronic schematics files that are used to make the PCB board

Third Party Resources and Useful Links:
----------------------
- [Micropython for the ESP8266 Read the Docs page](https://docs.micropython.org/en/latest/esp8266/index.html)
- [urequests.py micropython module](https://github.com/micropython/micropython-lib/blob/master/urequests/urequests.py)
- [Telegram Bots API](https://core.telegram.org/bots/api)
- [mpfshell github page](https://github.com/wendlers/mpfshell)
- [Nice article explaining how to hook up a LiPo battery to the ESP8266](https://randomnerdtutorials.com/esp8266-voltage-regulator-lipo-and-li-ion-batteries/)
- [EagleCAD Library for most/all ESP8266 variants](https://github.com/wvanvlaenderen/ESP8266-Eagle_Library)
- [OpenSCAD Socket Design for the ESP8266-07](https://github.com/makertum/ESP8266-RNS)
- [How to get the your telegram channel's id](https://github.com/GabrielRF/telegram-id#web-channel-id)
- [Eagle CAD library for Microchip components](https://www.element14.com/community/docs/DOC-64255/l/microchip-cad-library-for-cadsoft-eagle-software)
- [Eagle CAD library for basic parts by itead.cc (*like the BC557 PNP BJT*)](https://www.itead.cc/blog/eagle-library-for-basic-parts-series)