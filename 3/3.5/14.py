import json


name_file1 = input()
with open(name_file1, 'r', encoding='utf-8') as file1:
    users = json.load(file1)
with open(input(), 'r', encoding='utf-8') as file2:
    updates = json.load(file2)
result = {}
for i in users:
    for j in i:
        if j == 'name':
            result[i[j]] = {}
        else:
            result[i['name']][j] = i[j]
for i in updates:
    for j in i:
        if j != 'name':
            if j in result[i['name']]:
                if i[j] > result[i['name']][j]:
                    result[i['name']][j] = i[j]
            else:
                result[i['name']][j] = i[j]
with open(name_file1, 'w', encoding='utf-8') as file1:
    json.dump(result, file1, ensure_ascii=False)
