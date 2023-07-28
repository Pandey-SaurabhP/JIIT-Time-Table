import requests

url = 'http://127.0.0.1:5000'
data = 'key3'

x = requests.post(url, json=data)

print(x.text)
