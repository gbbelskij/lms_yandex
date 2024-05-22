from sys import stdin

summa = 0
numbers = []
for number in stdin:
    numbers.extend((number.rstrip('\n')).split())
for i in numbers:
    summa += int(i)
print(summa)
