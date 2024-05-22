n = int(input())
count = 0
for i in range(n):
    palind = input()
    error = False
    for i in range(len(palind) // 2):
        if palind[i] != palind[len(palind) - 1 - i]:
            error = True
    if not error:
        count += 1
print(count)
