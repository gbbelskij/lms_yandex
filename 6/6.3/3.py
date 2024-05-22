import requests


adress = input()
summa = 0
response = requests.get("http://" + adress).json()
for i in response:
    if isinstance(i, int):
        summa += i
print(summa)
