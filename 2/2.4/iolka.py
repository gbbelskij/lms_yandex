amount = int(input())
border = 1
i = 1
while i <= amount:
    for j in range(border):
        if i <= amount:
            print(i, end=' ')
        else:
            break
        i += 1
    border += 1
    print()
