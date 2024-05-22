numbers = {1, 2, 3, 4, 5}
print({i: ([j for j in range(1, i + 1) if i % j == 0]) for i in numbers})
