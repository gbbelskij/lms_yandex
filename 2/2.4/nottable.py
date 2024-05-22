n = int(input())
table = [[], []]
for i in range(2):
    for j in range(n):
        table[i].append(j + 1)
for i in range(n):
    for j in range(n):
        print(table[1][j], '*', table[0][i], '=', table[0][i] * table[1][j])
