from itertools import *

begin, ending, step = list(map(float, input().split()))
for i in count(begin, step):
    if i <= ending:
        print(round(i, 2))
    else:
        break
