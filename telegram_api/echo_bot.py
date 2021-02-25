import requests
import json
from pprint import pprint
import os
token = os.environ['TOKEN']
def getUpdates():
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    r = requests.get(url)
    data = r.json()
    updates = data['result']
    return updates

def sendMsg(idx,text):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': idx,
        'text': text,

    }
    r = requests.get(url, params=payload)

def getText(data):
    return data['text']

update_len = len(getUpdates())
update_len_last = len(getUpdates())



while True:
    update_len_last = len(getUpdates())
    message = getUpdates()[-1]['message']['text']

    if update_len != update_len_last:

        sendMessage(665551552,message)
        update_len = len(getUpdates())

