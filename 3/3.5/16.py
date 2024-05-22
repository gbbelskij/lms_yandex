from sys import stdin


lines = [line.strip('\n') for line in stdin]
string = lines[0].lower()
lines = lines[1:]
success = False
for name in lines:
    with open(name, encoding='utf-8') as file:
        file_s = file.read()
    file_s = file_s.lower()
    while '  ' in file_s or '\n' in file_s:
        if '  ' in file_s:
            file_s = file_s.replace('  ', ' ')
        if '\n' in file_s:
            file_s = file_s.replace('\n', ' ')
    if string in file_s:
        success = True
        print(name)
if not success:
    print('404. Not Found')
