n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
degree = int(input())
for i in numbers:
    ansv = 1
    for j in range(degree):
        ansv *= i
    print(ansv)
