def find_pair(*numbers, div=6):
    maxi = -10000000
    max1 = 0
    max2 = 0
    indmax2 = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            summa = numbers[i] + numbers[j]
            if summa % div == 0 and summa > maxi:
                    maxi = summa
                    max1 = numbers[i]
                    max2 = numbers[j]
                    indmax2 = j
            elif summa % div == 0 and summa == maxi:
                if j > indmax2:
                    maxi = summa
                    max1 = numbers[i]
                    max2 = numbers[j]
                    indmax2 = j
    return (max1, max2)

numbers = [1, 2, 3, 4, 5]
result = find_pair(*numbers)
print(*result)
