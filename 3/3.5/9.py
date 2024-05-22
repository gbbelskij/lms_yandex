name_file1, name_file2 = input(), input()
with open(name_file1, encoding='utf-8') as file1:
    file_s = file1.read()
while '  ' in file_s or '\t' in file_s or '\n\n' in file_s or '\n ' in file_s or ' \n' in file_s:
    if '  ' in file_s:
        file_s = file_s.replace('  ', ' ')
    if '\t' in file_s:
        file_s = file_s.replace('\t', '')
    if '\n\n' in file_s:
        file_s = file_s.replace('\n\n', '\n')
    if '\n ' in file_s:
        file_s = file_s.replace('\n ', '\n')
    if ' \n' in file_s:
        file_s = file_s.replace(' \n', '\n')
if file_s[0] == ' ':
    file_s = file_s.replace(' ', '', 1)
with open(name_file2, 'w', encoding='utf-8') as file2:
    file2.write(file_s)
