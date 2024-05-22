import itertools

kids1 = list(input().split(', '))
kids2 = list(input().split(', '))
for i in list(zip(kids1, kids2)):
    print(i[0], i[1], sep=' - ')
