n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
s1 = k1 - m
s2 = m - k2
print(int(n - n * (s1 / (s1 + s2))), int(n * (s1 / (s1 + s2))))
