import network

class NetworkManager(object):
    _sta_if = network.WLAN(network.STA_IF)
    _ap_if = network.WLAN(network.AP_IF)

    @staticmethod
    def init():
        """Initialize ESP8266 in Wireless Station mode"""
        NetworkManager._ap_if.active(False)
        NetworkManager._sta_if.active(True)    
    
    # TODO: add timeout for conecting to network
    @staticmethod
    def connect(ssid, password):
        """Connect to the wifi with the given ssid and password"""
        st_if = NetworkManager._sta_if
        # Make sure the Station interface is active
        if not st_if.active():
            NetworkManager.init()
        # If the device is not already connected to a network
        if not st_if.isconnected():
            st_if.connect(ssid, password)
            # wait for connection to succeed
            while not st_if.isconnected():
                pass
            print("[info] connected to network:", st_if.ifconfig())
        else:
            print("[info] already connected to network:", st_if.ifconfig())
            
    @staticmethod
    def disconnect():
        NetworkManager._sta_if.disconnect()
