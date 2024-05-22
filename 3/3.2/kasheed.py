n = int(input())
m = int(input())
array1 = []
count = 0
for i in range(n):
    array1.append(input())
for i in range(m):
    if input() in array1:
        count += 1
if count > 0:
    print(count)
else:
    print('Таких нет')
