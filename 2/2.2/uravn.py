import math


a, b, c = int(input()), int(input()), int(input())
d = b * b - 4 * a * c
x1 = (b * -1 + math.sqrt(d)) / (2 * a)
x2 = (b * -1 - math.sqrt(d)) / (2 * a)
if x1 == x2:
    print(round(x1, 2))
else:
    print(round(x1, 2), round(x2, 2))
