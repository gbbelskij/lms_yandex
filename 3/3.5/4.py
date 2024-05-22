from sys import stdin

lines = []
for line in stdin:
    lines.append(line.rstrip('\n'))
for i in range(len(lines) - 1):
    if lines[-1].lower() in lines[i].lower():
        print(lines[i])
