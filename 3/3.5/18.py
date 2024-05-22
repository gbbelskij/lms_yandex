import os
import math

name = input()
b = 'Б'
amount = 0
with open(name, 'rb') as file:
    while True:
        byte = file.read(1)
        if not byte:
            break
        amount += 1
if amount > 1024:
    amount = math.ceil(amount / 1024)
    b = 'КБ'
if amount > 1024:
    amount = math.ceil(amount / 1024)
    b = 'МБ'
if amount > 1024:
    amount = math.ceil(amount / 1024)
    b = 'ГБ'
print(amount, b, sep='')
