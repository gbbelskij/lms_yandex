from sys import stdin
from math import gcd


for line in stdin:
    lines = list(map(int, line.rstrip('/n').split()))
    print(gcd(*lines))
