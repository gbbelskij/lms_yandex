n, m = int(input()), int(input())
children = []
flag = False  # флаг того, что есть ребенок, который любит 1 кашу
for i in range(n + m):
    child = input()
    if child not in children:
        children.append(child)
    else:
        children.pop(child)
children.sort()
for i in children:
    print(i)
    flag = True
if not flag:
    print('Таких нет')
