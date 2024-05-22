string = input()
string = string.lower()
string = string.replace(' ', '')
flag = True
for i in range(len(string) // 2):
    if string[i] != string[len(string) - 1 - i]:
        flag = False
if flag:
    print('YES')
else:
    print('NO')
