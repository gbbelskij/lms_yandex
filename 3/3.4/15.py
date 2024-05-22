from itertools import permutations

n = int(input())
products = [i for _ in range(n) for i in list(input().split(', '))]
products.sort()
for i in permutations(products, 3):
    print(*i)
