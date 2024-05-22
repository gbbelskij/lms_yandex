from itertools import *

n = int(input())
purchase = []
for i in range(n):
    purchase.append(list(input().split(', ')))
for i in enumerate(sorted(set(chain.from_iterable(purchase))), 1):
    print(f"{i[0]}. {i[1]}")
