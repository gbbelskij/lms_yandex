with open('secret.txt', encoding='utf-8') as file:
    string = file.read()
result = ''
for i in string:
    if ord(i) < 128:
        result += i
    else:
        result += chr(ord(i) & 255)
print(result)
