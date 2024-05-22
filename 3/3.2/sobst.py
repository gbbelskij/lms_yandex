n = int(input())
kids = {}
for _ in range(n):
    name, toys = input().split(': ')
    set_toys = set(toys.split(', '))
    kids[name] = set_toys
result = set()
for i in kids:
    toys = kids[i].copy()
    for j in kids:
        if i != j:
            toys.difference_update(kids[j])
    result.update(toys)
print(*sorted(list(result)), sep='\n')
