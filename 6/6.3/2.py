import requests


adress = input()
res = 1
summa = 0
while res != 0:
    res = requests.get("http://" + adress).content.decode("utf-8")
    summa += int(res)
print(summa)
