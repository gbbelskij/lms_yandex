def sort(s):
    temp = [i for i in s]
    res = ''
    for i in range(len(s)):
        for j in range(len(s)):
            if temp[i] < temp[j]:
                temp[i], temp[j] = temp[j], temp[i]
    for i in temp:
        res += i
    return res

def counter(text):
    text = text.replace(' ', '')
    text = sort(text)
    while text != '':
        yield (text[0], text.count(text[0]))
        text = text.replace(text[0], '')

text = 'Мама мыла раму'
for letter, count in counter(text):
    print(letter, count)
