n = int(input())
result = []
for i in range(n):
    result += input().split()
for i in set(result):
    print(i)
