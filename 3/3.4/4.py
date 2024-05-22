from itertools import *

s = [i + ' ' for i in list(input().split())]
for i in accumulate(s):
    print(i)
