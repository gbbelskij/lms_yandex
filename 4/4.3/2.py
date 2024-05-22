def recursive_digit_sum(s):
    if s < 10:
        return s
    return s % 10 + recursive_digit_sum(s // 10)

print(recursive_digit_sum(123))
