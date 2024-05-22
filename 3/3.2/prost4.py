from functools import lru_cache


@lru_cache(None)
def delit(n):
    result = set()
    for i in range(1, abs(n) + 1):
        if abs(n) % i == 0:
            result.add(i)
    return result


numbers = {int(i) for i in input().split('; ')}
simple = {}
for i in numbers:
    simple[i] = []
    for j in numbers:
        if i != j:
            if len(delit(i).intersection(delit(j))) == 1:
                simple[i].append(j)
for i in sorted(simple.keys()):
    if len(simple[i]) > 0:
        print(f"{i} - ", end='')
        print(*sorted(simple[i]), sep=', ')
