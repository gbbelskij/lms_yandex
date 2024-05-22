string = input()
print('a b c f')
for i in range(8):
    values = list('0' * (3 - len(bin(i)[2:])) + bin(i)[2:])
    a, b, c = map(int, values)
    print(' '.join(values), int(eval(string)))
