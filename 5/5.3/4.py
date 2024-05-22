def only_positive_even_sum(a, b):
    if not all(isinstance(i, int) for i in (a, b)):
        raise TypeError
    if not all(i > 0 and i % 2 == 0 for i in (a, b)):
        raise ValueError
    return a + b

print(only_positive_even_sum(-5, 4))
