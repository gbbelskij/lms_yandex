def can_eat(f, s):
    fx, fy = f[0], f[1]
    eatable = ((fx + 2, fy + 1), (fx + 2, fy - 1), (fx - 2, fy + 1),
            (fx - 2, fy - 1), (fx + 1, fy + 2), (fx + 1, fy - 2),
            (fx - 1, fy + 2), (fx - 1, fy - 2))
    if any(i == s for i in eatable if all(j > 0 for j in i)):
        return True
    return False

print(can_eat((2, 1), (4, 2)))
