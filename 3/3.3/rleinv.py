rle = [('a', 2), ('b', 3), ('c', 1)]
string = ''
for i in range(len(rle)):
    for j in range(rle[i][1]):
        string += rle[i][0]
print(string)
