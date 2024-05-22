n = int(input())
children = {}
for i in range(n):
    string = input().split()  # входные данные
    name = string[0]
    for pork in range(1, len(string)):
        if string[pork] not in children:
            children[string[pork]] = name + ' '
        else:
            children[string[pork]] += name + ' '
concrete_pork = input()
if concrete_pork in children:
    answer = children[concrete_pork].split()
    answer.sort()
    for i in answer:
        print(i)
else:
    print('Таких нет')
