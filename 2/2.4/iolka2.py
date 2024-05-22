def width_of_line(array):
    width = len(' ' * (len(array) - 1))
    for i in array:
        width += len(str(i))
    return width


n = int(input())
array = []
border = 1
element = 1
while element <= n:
    array_line = []
    for i in range(border):
        if element <= n:
            array_line.append(element)
            element += 1
    array.append(array_line)
    border += 1
if len(array) > 1 and len(array[-2]) > len(array[-1]):
    width = width_of_line(array[-2])
else:
    width = width_of_line(array[-1])
for i in array:
    print(' ' * ((width - width_of_line(i)) // 2), end='')
    for j in i:
        print(j, end=' ')
    print()
