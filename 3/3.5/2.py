from sys import stdin

people = []
for line in stdin:
    people.append(line.rstrip('\n').split())
height = 0
count = 0
for i in people:
    height += int(i[2]) - int(i[1])
    count += 1
print(round(height / count))
