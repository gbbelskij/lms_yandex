n = int(input())
m = int(input())
count = 1
length = len(str(n * m))
array = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        array[i][j] = count
        count += 1
reverse = 0
for i in range(n):
    if reverse % 2 != 0:
        for j in range(m):
            print(' ' * (length - len(str(array[i][m - 1 - j]))), array[i][m - 1 - j], end=' ', sep='')
        print()
    else:
        for j in range(m):
            print(' ' * (length - len(str(array[i][j]))), array[i][j], end=' ', sep='')
        print()
    reverse += 1
