from itertools import *

n = int(input())
count = 1
list_of = [i for i in range(1, n + 1)]
for i in product(list_of, list_of):
    if count > n:
        print()
        count = 1
    print(i[0] * i[1], end=' ')
    count += 1
