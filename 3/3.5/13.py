import json
from sys import stdin

lines = [line.strip('\n') for line in stdin]
with open(lines[0], encoding='utf-8') as file1:
    record = json.load(file1)
for i in range(1, len(lines)):
    key, value = lines[i].split(' == ')
    record[key] = value
with open(lines[0], 'w', encoding='utf-8') as file_out:
    json.dump(record, file_out, ensure_ascii=False)
