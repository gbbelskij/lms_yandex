def gcd(*args):
    for i in range(min(args), 0, -1):
        flag = True
        for j in args:
            if j % i != 0:
                flag = False
        if flag:
            return i

print(gcd(36, 48, 156, 100500))
