import math


n = int(input())
simple = []
answer = []
for i in range(2, n):
    counti = 0
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            counti += 1
    if counti == 0:
        simple.append(i)
i = 2
final = n
while n > 1 and i < final:
    if i in simple and n % i == 0:
        answer.append(i)
        n //= i
        i = 1
    i += 1
for i in range(len(answer)):
    if i != len(answer) - 1:
        print(answer[i], end=' * ')
    else:
        print(answer[i])
