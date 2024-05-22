numbers = []

def add_number(n):
    numbers.append(n)

def get_sum():
    s = ' + '.join(map(str, numbers)) + ' = ' + str(sum(numbers))
    return s

add_number(1)
add_number(2)
add_number(3)
print(get_sum())
