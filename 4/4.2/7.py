def enter_results(*args):
    global exp
    exp += [i for i in args]

def get_sum():
    global exp
    sum1 = 0
    sum2 = 0
    for i in exp[::2]:
        sum1 += i
    for i in exp[1::2]:
        sum2 += i
    return (sum1, sum2)

def get_average():
    global exp
    average1 = 0
    average2 = 0
    for i in exp[::2]:
        average1 += i
    for i in exp[1::2]:
        average2 += i
    return (round(average1 / len(exp[::2]), 2), round(average2 / len(exp[::2]), 2))

exp = list()

enter_results(1, 2, 3, 4, 5, 6)
print(get_sum(), get_average())
enter_results(1, 2)
print(get_sum(), get_average())
