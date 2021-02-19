import requests
import json
from pprint import pprint
token = '1686665754:AAHyBYlpebtmliH256xnQW7_7J4D2nJRtjo'

url=f'https://api.telegram.org/bot{token}/sendMessage'
#id=665551552
r = requests.get(url)

