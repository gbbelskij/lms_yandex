from sys import stdin

lines = []
for line in stdin:
    lines.extend(line.rstrip('\n').split())
answer = []
print(lines)
for i in lines:
    if len(i) > 1:
        if i[:len(i) // 2].lower() == (i[len(i) // 2 + 1:])[::-1].lower():
            answer.append(i)
    else:
        answer.append(i)
print(*sorted(set(answer)), sep='\n')
