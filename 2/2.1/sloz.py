def f(n, arr):
    arr.append(n // 100)
    arr.append((n - n % 10) // 10 % 10)
    arr.append(n % 10)
    #print(arr)
    return arr


n1 = int(input())
n2 = int(input())
num1 = []
num2 = []
num1 = f(n1, num1)
num2 = f(n2, num2)
for i in range(3):
    print((num1[i] + num2[i]) % 10, end="")
