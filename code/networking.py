import network
import time

class NetworkManager(object):
    _sta_if = network.WLAN(network.STA_IF)
    _ap_if = network.WLAN(network.AP_IF)

    @staticmethod
    def init():
        """Initialize ESP8266 in Wireless Station mode"""
        NetworkManager._ap_if.active(False)
        NetworkManager._sta_if.active(True)    

    @staticmethod
    def isconnected():
        """Returnes True if the device is already connected"""
        return NetworkManager._sta_if.isconnected()
    
    @staticmethod
    def connect(ssid, password, timeout=5):
        """Connect to the wifi with the given ssid and password
        @param ssid: The SSID of the network to connect to
        @param password: The password of the network to connect to
        @param timeout: Optional parameters specifying the maximum seconds to wait before giving up (must be an integer)
        """
        st_if = NetworkManager._sta_if
        # Make sure the Station interface is active
        if not st_if.active():
            NetworkManager.init()
        # If the device is not already connected to a network
        if not NetworkManager.isconnected():
            st_if.connect(ssid, password)
            # wait for connection to succeed
            deadline = time.time() + timeout
            while not st_if.isconnected() and time.time() < deadline:
                pass
            if st_if.isconnected():
                print("[info] connected to network (%s):" % ssid, st_if.ifconfig())
                return True
            else:
                print("[info] timeout while tying to connect to network (%s)" % ssid)
                st_if.disconnect()
                return False
        else:
            print("[info] already connected to network:", st_if.ifconfig())
            
    @staticmethod
    def disconnect():
        NetworkManager._sta_if.disconnect()
