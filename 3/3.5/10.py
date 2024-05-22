name_file = input()
n = int(input())
with open(name_file, encoding='utf-8') as file:
    strings = [line.strip('\n') for line in file.readlines()]
for i in range(len(strings) - n, len(strings)):
    print(strings[i])
