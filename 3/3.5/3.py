from sys import stdin

lines = []
for line in stdin:
    if '#' in line:
        if line[0] != '#':
            lines.append(line.rstrip('\n').split('#')[0])
    else:
        lines.append(line.rstrip('\n'))
print(*lines, sep='\n')
