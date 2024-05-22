n = int(input())
m = int(input())
count = 1
length = len(str(n * m))
array = [[0 for i in range(n)] for j in range(m)]
for i in range(m):
    for j in range(n):
        array[i][j] = count
        count += 1
    if i % 2 != 0:
        array[i].reverse()
for i in range(n):
    for j in range(m):
        print(' ' * (length - len(str(array[j][i]))), array[j][i], end=' ', sep='')
    print()
