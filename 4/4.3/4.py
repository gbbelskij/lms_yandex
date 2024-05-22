def answer(f):
    def decorated(*args, **kwargs):
        return 'Результат функции: ' + str(f(*args, **kwargs))
    return decorated

@answer
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5))
