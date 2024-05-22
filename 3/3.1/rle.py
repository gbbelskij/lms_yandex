string = input()
count = 1
for i in range(len(string) - 1):
    if string[i] == string[i + 1]:
        count += 1
    else:
        print(string[i], count)
        count = 1
print(string[-1], count)
