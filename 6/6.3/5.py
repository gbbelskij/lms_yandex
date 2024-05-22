from requests import get
from sys import stdin


adress = input()
paths = list(i.rstrip('\n') for i in stdin)
summa = 0

for i in paths:
    summa += sum(get("http://" + adress + i).json())

print(summa)
