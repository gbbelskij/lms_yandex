import math


x = input()
if '.' in x:
    x = float(x)
else:
    x = int(x)
print(math.log(pow(x, 3 / 16), 32) + pow(x, math.cos(math.pi * x / (2 * math.e))) - pow(math.sin(x / math.pi), 2))
