from itertools import *

n = int(input())
porrige = [input() for _ in range(n)]
days = int(input())
count = 1
for i in cycle(porrige):
    if count <= days:
        print(i)
        count += 1
    else:
        break
