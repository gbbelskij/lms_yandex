str1 = '᥈୥ᙬᱬᝯ, ᭷ᝯ୲੬๤!'
#print(''.join(chr(ord(i) & 255) for i in str1))
result = ''
for i in str1:
    if ord(i) < 128:
        result += i
    else:
        result += chr(ord(i) & 255)
print(result)
