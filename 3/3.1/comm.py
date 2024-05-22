string = input()
while string != '':
    if '#' in string:
        if '#' != string[0]:
            for i in range(len(string)):
                if string[i] != '#':
                    print(string[i], end='')
                else:
                    break
            print()
    else:
        print(string)
    string = input()
