x = 0
y = 0
direct = ''
while direct != 'STOP':
    direct = input()
    if direct == 'STOP':
        break
    n = int(input())
    if direct == 'СЕВЕР':
        y += n
    elif direct == 'ВОСТОК':
        x += n
    elif direct == 'ЮГ':
        y -= n
    elif direct == 'ЗАПАД':
        x -= n
print(x, y, sep='\n')
