all_num = 0
plus = 0
minus = 0
maxi = -1000000000
mini = 1000000000
summa = 0
middle = 0
name_file = input()
with open(name_file, encoding='utf-8') as file:
    for i in file:
        for j in i.split():
            number = int(j)
            if number > 0:
                plus += 1
            if number < 0:
                minus += 1
            maxi = max(maxi, number)
            mini = min(mini, number)
            summa += number
            all_num += 1
    middle = round(summa / all_num, 2)
print(all_num, plus, minus, maxi, mini, summa, middle, sep='\n')
