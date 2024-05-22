def change_base(number, base):
    res = ''
    while number > 0:
        res += str(number % base)
        number //= base
    return res[::-1]


number = int(input())
max_summa = 0
max_base = 0
for i in range(2, 11):
    summa = 0
    for j in change_base(number, i):
        summa += int(j)
    if summa > max_summa:
        max_summa = summa
        max_base = i
print(max_base)
