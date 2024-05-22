from itertools import *

n = int(input())
sportsmen = [input() for _ in range(n)]
for i in permutations(sorted(sportsmen)):
    print(*i, sep=', ')
