import requests


response = requests.get(url="http://127.0.0.1:5000")
print(response.content.decode("utf-8"))
