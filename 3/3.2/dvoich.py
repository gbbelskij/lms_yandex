string = input().split()
result = []
for i in string:
    statistic = {}
    number = int(i)
    number = bin(number)[2:]
    statistic["digits"] = len(number)
    statistic["units"] = number.count('1')
    statistic["zeros"] = number.count('0')
    result.append(statistic)
print(result)
