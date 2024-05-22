import json
from sys import stdin

lines = [line.strip('\n') for line in stdin]
with open('scoring.json', 'r', encoding='utf-8') as file:
    score = json.load(file)
index = 0
all_points = 0
for i in score:
    success = 0
    points = i['points']
    for j in i['tests']:
        if j['pattern'] == lines[index]:
            success += 1
        index += 1
    all_points += round(success / len(i['tests']) * points)
print(all_points)
