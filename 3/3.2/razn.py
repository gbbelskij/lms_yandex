string1 = set(input())
string2 = set(input())
result = []
for i in string1:
    if i in string2:
        print(i, end='')
