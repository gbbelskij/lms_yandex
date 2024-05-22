def is_palindrome(n):
    if isinstance(n, int):
        if str(n)[:len(str(n)) // 2] == str(n)[-1: len(str(n)) - 1 - len(str(n)) // 2: -1]:
            return True
        return False
    else:
        if n[:len(n) // 2] == n[-1: len(n) - 1 - len(n) // 2: -1]:
            return True
        return False

s = 'abacdaba'
l = [1, 2, 3, 2, 2, 1]
t = (1, 2, 3, 2, 1)
i = 12321
for j in i, s, t, l:
    print(is_palindrome(j))
