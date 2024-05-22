from itertools import *

n = int(input())
sportsmen = [input() for _ in range(n)]
sportsmen.sort()
for i in permutations(sportsmen, 3):
    print(*i, sep=', ')
