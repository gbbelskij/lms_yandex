n = int(input())
width = int(input())
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
        prev_space = ' ' * ((width - len(str(table[i][j]))) // 2)
        post_space = ' ' * (width - ((width - len(str(table[i][j]))) // 2) - len(str(table[i][j])))
        if j != n - 1:
            print(prev_space, table[i][j], post_space, sep='', end='|')
        else:
            print(prev_space, table[i][j], post_space, sep='', end='')
    print()
    if i != n - 1:
        print("-" * width * n + '-' * (n - 1))
