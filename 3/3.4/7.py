from itertools import *

competitors = []
n = int(input())
for _ in range(n):
    competitors.append(input())
for i in combinations(competitors, 2):
    print(i[0], i[1], sep=' - ')
