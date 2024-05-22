terrain = input()
result = set()
while terrain != '':
    array_terrain = terrain.split()
    for i in range(1, len(array_terrain) - 1):
        if array_terrain[i] == 'зайка':
            result.add(array_terrain[i + 1])
            result.add(array_terrain[i - 1])
    if array_terrain[-1] == 'зайка':
        result.add(array_terrain[-2])
    if array_terrain[0] == 'зайка':
        result.add(array_terrain[1])
    terrain = input()
for i in result:
    print(i)
