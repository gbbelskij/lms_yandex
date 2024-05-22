length = int(input())
length -= len('...')
n = int(input())
s = [input() for i in range(n)]
for string in s:
    if length >= len(string):
        length -= len(string)
        if length <= 0:
            print(string, '...', sep='')
            break
        else:
            print(string)
    else:
        print(string[:length], '...', sep='')
        break
