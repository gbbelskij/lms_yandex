n = int(input())
table = [[] for i in range(n)]
for j in range(n):
    table[0].append(j + 1)
for i in range(n):
    table[i].append(i + 1)
for i in range(1, n):
    for j in range(1, n):
        table[i].append(table[0][j] * table[i][0])
for i in range(n):
    for j in range(n):
        print(table[i][j], end=' ')
    print()
