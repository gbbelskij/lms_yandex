def f(n):
    if n <= 9:
        return "0" + str(n)
    else:
        return str(n)


n = int(input())
m = int(input())
t = int(input())
n += t // 60
m += t % 60
n = n % 24
print(f(n), ":", f(m), sep="")
