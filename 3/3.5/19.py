shift = int(input())
with open('public.txt', encoding='utf-8') as file:
    string = file.read().strip('\n')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = ''
for i in string:
    if i.lower() in alphabet:
        ind = alphabet.find(i.lower()) + shift
        ind %= len(alphabet)
        if i.islower():
            result += alphabet[ind]
        elif i.isupper():
            result += alphabet[ind].upper()
    else:
        result += i
with open('private.txt', 'w', encoding='utf-8') as file_out:
    file_out.write(result)
