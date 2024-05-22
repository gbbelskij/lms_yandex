n = int(input())
if n % 2 != 0:
    width = len(str((n + 1) // 2))
else:
    width = len(str(n // 2))
for i in range(n):
    for j in range(n):
        number = str(min(i + 1, j + 1, n - i, n - j))
        if j < n - 1:
            print(' ' * (width - len(number)), number, sep='', end=' ')
        else:
            print(' ' * (width - len(number)), number, sep='', end='\n')
