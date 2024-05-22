n = int(input())
staff = {}
for i in range(n):
    worker = input()
    if worker not in staff:
        staff[worker] = 1
    else:
        staff[worker] += 1
flag = False  # флаг, есть ли однофамильцы
staff = sorted(staff.items())
for i in staff:
    if i[1] > 1:
        print(f"{i[0]} - {i[1]}")
        flag = True
if not flag:
    print('Однофамильцев нет')
