import math


class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if not all(isinstance(i, float) or isinstance(i, int) for i in (a, b, c)):
        raise TypeError
    d = b * b - 4 * a * c
    if a == 0:
        if b == 0:
            if c == 0:
                raise InfiniteSolutionsError
            else:
                raise NoSolutionsError
        else:
            return (-c / b)
    else:
        if d < 0:
            raise NoSolutionsError
        else:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            return min(x1, x2), max(x1, x2)
