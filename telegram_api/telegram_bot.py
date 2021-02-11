import requests
token = '1686665754:AAHyBYlpebtmliH256xnQW7_7J4D2nJRtjo'

url=f'https://api.telegram.org/bot{token}/getMe'

r = requests.get(url)
print(r.json())