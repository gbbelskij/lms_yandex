n = int(input())
m = int(input())
length = len(str(n * m))
count = 1
for i in range(n):
    for j in range(m):
        print(' ' * (length - len(str(count))), count, end=' ', sep='')
        count += 1
    print()
