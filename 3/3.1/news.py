length = int(input())
n = int(input())
for i in range(n):
    string = input()
    if len(string) <= length:
        print(string)
    else:
        print(f"{string[:(length - len('...'))]}...")
