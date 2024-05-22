n = int(input())
h_last = 0
error = -1
for i in range(n):
    b = int(input())
    h = b % 256
    r = b // 256 % 256
    m = b // 256 ** 2
    h_now = 37 * (r + m + h_last) % 256
    if h >= 100 or h != h_now:
        error = i
        break
    h_last = h
if error == -1:
    print(-1)
