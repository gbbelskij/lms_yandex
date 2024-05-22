import math


n = int(input())
answer = 0
for _ in range(n):
    number = int(input())
    count = 0
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            count += 1
    if count == 0 and number != 1:
        answer += 1
print(answer)
