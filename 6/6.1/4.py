import math


num = list(map(float, input().split()))
print(pow(math.prod(num), 1 / len(num)))
