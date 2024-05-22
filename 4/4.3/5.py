def result_accumulator(f):
    res = []

    def decorated(*args, method='accumulate'):
        nonlocal res
        res.append(f(*args))
        if method == 'drop':
            tmp = res
            res = []
            return tmp
    return decorated

@result_accumulator
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))
