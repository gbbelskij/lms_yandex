string = input()
terrain = {}
while string != '':
    for i in string.split():
        if i not in terrain:
            terrain[i] = 1
        else:
            terrain[i] += 1
    string = input()
for i in terrain:
    print(i, terrain[i])
