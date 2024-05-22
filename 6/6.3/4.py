from requests import get


adress = input()
key = input()
response = get("http://" + adress).json()
try:
    print(response[key])
except KeyError:
    print("No data")
