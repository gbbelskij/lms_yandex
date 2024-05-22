up = 1001
half = 500
down = 0
answer = ''
while answer != 'Угадал!':
    print(half)
    answer = input()
    if answer == 'Больше':
        down = half
        half = (up + down) // 2
    elif answer == 'Меньше':
        up = half
        half = (up + down) // 2
