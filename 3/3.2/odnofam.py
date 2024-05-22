n = int(input())
staff = {}
count = 0
for i in range(n):
    worker = input()
    if worker not in staff:
        staff[worker] = 1
    else:
        staff[worker] += 1
for i in staff:
    if staff[i] > 1:
        count += staff[i]
print(count)
