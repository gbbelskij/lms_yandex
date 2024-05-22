letters = {}
word = input()
while word != 'ФИНИШ':
    for i in word.lower():
        if i != ' ':
            if i not in letters:
                letters[i] = 0
                letters[i] += 1
            else:
                letters[i] += 1
    word = input()
max_char = ''
max_times = -1
for i in sorted(letters, reverse=1):
    if letters[i] >= max_times:
        max_times = letters[i]
        max_char = i
print(max_char)
