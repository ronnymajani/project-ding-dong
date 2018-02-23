try:  # CPython
    import requests
    import json
except ImportError:  # Micropython
    import urequests
    import usjon


class TelegramBot(object):
    def __init__(self, token):
        self.token = token
        self.url = "https://api.telegram.org/bot%s" % self.token

    def _build_url(self, method_name):
        return self.url + "/%s" % method_name

    def _send_request(self, method_name, params):
        url = self._build_url(method_name)
        requests.get(url, params=params)

    def sendMessage(self, chatid, text):
        params = {
            'chat_id': chatid,
            'text': text
        }
        self._send_request('sendMessage', params)