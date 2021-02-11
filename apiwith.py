import requests
url = 'https://randomuser.me/api/'
payload = {'results':2, 'gender':'male'}




r = requests.get(url,payload)
data=r.json()['results']
for i in data:
    print(i['name'], i['nat'])