def changer2(array, a):
    array.pop()
    array.pop()
    array.append(a)
    return array

def changer1(array, a):
    array.pop()
    array.append(a)
    return array

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

string = input().split()
numbers = []
actions = []
for i in string:
    if i in '+-*/~!#@':
        if i == '+':
            new_number = numbers[-1] + numbers[-2]
            numbers = changer2(numbers, new_number)
        elif i == '*':
            new_number = numbers[-1] * numbers[-2]
            numbers = changer2(numbers, new_number)
        elif i == '-':
            new_number = numbers[-2] - numbers[-1]
            numbers = changer2(numbers, new_number)
        elif i == '/':
            new_number = numbers[-2] // numbers[-1]
            numbers = changer2(numbers, new_number)
        elif i == '~':
            new_number = -1 * numbers[-1]
            numbers = changer1(numbers, new_number)
        elif i == '!':
            new_number = factorial(numbers[-1])
            numbers = changer1(numbers, new_number)
        elif i == '#':
            new_number = numbers[-1]
            numbers.append(new_number)
        elif i == '@':
            new_numbers = [numbers[-2], numbers[-1], numbers[-3]]
            numbers.pop()
            numbers.pop()
            numbers.pop()
            numbers += new_numbers
    else:
        numbers.append(int(i))
print(*numbers)
