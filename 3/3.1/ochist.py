s = input()
while s != '':
    if s[-3:] != '@@@':
        if s[0:2] == '##':
            s = s[2:]
        print(s)
    s = input()
