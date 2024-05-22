n = int(input())
number_max = 0
answer = ''
for _ in range(n):
    number = input()
    for i in number:
        number_max = max(number_max, int(i))
    answer += str(number_max)
print(answer)
