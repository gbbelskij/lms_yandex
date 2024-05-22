n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
for i in range(min(numbers), 0, -1):
    count = 0
    for j in numbers:
        if j % i == 0:
            count += 1
    if count == n:
        print(i)
        break
