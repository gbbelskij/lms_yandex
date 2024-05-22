n = int(input())
for i in range(n):
    view = input()
    success = 0
    for j in range(len(view)):
        if view[j:(j + len('зайка'))] == 'зайка':
            print(j + 1)
            success += 1
            break
    if not bool(success):
        print('Заек нет =(')
