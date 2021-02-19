import requests
import json
from pprint import pprint
token = '1686665754:AAHyBYlpebtmliH256xnQW7_7J4D2nJRtjo'

url=f'https://api.telegram.org/bot{token}/sendMessage'
payload={
    'chat_id':480822009,
    'text':'YOMON AYIQ, QUNGIR PUNGIR AYIQ'
}
r = requests.get(url,params=payload)
print(r.json())
