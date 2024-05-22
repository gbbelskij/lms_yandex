def stop_iteration(*args):
    for i in args:
        try:
            iter(i)
        except TypeError:
            raise StopIteration


def type_error(*args):
    i = []
    for j in args:
        i.extend(list(j))
    if not all(type(member) is type(i[0]) for member in i):
        raise TypeError


def value_error(*args):
    for i in args:
        if list(i) != sorted(i):
            raise ValueError
    return True


def merge(a, b):
    stop_iteration(a, b)
    type_error(a, b)
    value_error(a, b)
    a_1 = list(a)
    b_1 = list(b)
    ans = []
    while a_1 and b_1:
        if a_1[0] > b_1[0]:
            ans.append(b_1.pop(0))
        else:
            ans.append(a_1.pop(0))
    ans.extend(a_1 + b_1)
    return ans
