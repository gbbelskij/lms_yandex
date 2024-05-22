def fibonacci(n):
    first = 0
    second = 1
    for _ in range(n):
        yield first
        first, second = second, first + second

print(*fibonacci(5))
