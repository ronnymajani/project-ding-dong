import requests
try:  # CPython
    import json
except ImportError:  # Micropython
    import ujson as json

class TelegramBot(object):
    def __init__(self, token):
        self.token = token
        self.url = "https://api.telegram.org/bot%s" % self.token

    def _build_url(self, method_name):
        return self.url + "/%s" % method_name

    def _send_request(self, method_name, params):
        url = self._build_url(method_name)
        response = requests.get(url, json=params)
        success = response.json()['ok']
        if success:
            print("Successfully sent message")
        else:
            print("[error] Failed to send message")
        response.close()
        return success

    def sendMessage(self, chatid, text):
        # url += "?chat_id=%s&text=%s" % (chatid, 'test')
        params = {
            'chat_id': chatid,
            'text': text
        }
        self._send_request('sendMessage', params)