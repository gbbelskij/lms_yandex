def merge(a, b):
    tup = list(a + b)
    for i in range(len(tup) - 1):
        for j in range(len(tup) - i - 1):
            if tup[j] > tup[j + 1]:
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tuple(tup)

print(merge((1, 7, 9), (2, 4, 11)))
