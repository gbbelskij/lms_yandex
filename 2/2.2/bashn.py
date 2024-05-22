def f(n):
    return (n // 10, n % 10)


num1, num2, num3 = int(input()), int(input()), int(input())
num1did1, num1did2 = f(num1)
num2did1, num2did2 = f(num2)
num3did1, num3did2 = f(num3)
for i in num1did1, num1did2:
    for j in num2did1, num2did2:
        for k in num3did1, num3did2:
            if i == j and j == k:
                print(i)
                break
