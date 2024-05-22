n = int(input())
m = int(input())
width = len(str(n * m))
count = 1
for i in range(1, n * m + 1):
    if count > m:
        print()
        count = 1
    print(' ' * (width - len(str(i))), i, end=' ', sep='')
    count += 1
