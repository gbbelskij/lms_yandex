string = input().split()
degree = int(input())
for i in range(len(string)):
    string[i] = int(string[i]) ** degree
print(*string)
