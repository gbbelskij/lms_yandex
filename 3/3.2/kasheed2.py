n, m = int(input()), int(input())
children = {}
count = 0  # счётчик любителей одной каши
for i in range(n + m):
    child = input()
    if child not in children:
        children[child] = 1
        count += 1
    else:
        children[child] += 1
        count -= 1
if count > 0:
    print(count)
else:
    print('Таких нет')
