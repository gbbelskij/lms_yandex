import json


name_file1, name_file2 = input(), input()
count = 0
positive_count = 0
mini = 10000000000
maxi = -10000000000
summa = 0
average = 0
with open(name_file1, encoding='utf-8') as file1:
    ints = [i.strip('\n') for i in file1.readlines()]
    for i in ints:
        for j in i.split():
            temp = int(j)
            count += 1
            if temp > 0:
                positive_count += 1
            mini = min(mini, temp)
            maxi = max(maxi, temp)
            summa += temp
average = round(summa / count, 2)
answer = {
    "count": count,
    "positive_count": positive_count,
    "min": mini,
    "max": maxi,
    "sum": summa,
    "average": average
}
with open(name_file2, 'w', encoding='utf-8') as file2:
    json.dump(answer, file2, ensure_ascii=False)
