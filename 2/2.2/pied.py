p, v, t = int(input()), int(input()), int(input())
if p >= v and v >= t:
    first = "Петя"
    second = "Вася"
    third = "Толя"
elif p >= t and t >= v:
    first = "Петя"
    second = "Толя"
    third = "Вася"
elif v >= t and t >= p:
    first = "Вася"
    second = "Толя"
    third = "Петя"
elif v >= p and p >= t:
    first = "Вася"
    second = "Петя"
    third = "Толя"
elif t >= p and p >= v:
    first = "Толя"
    second = "Петя"
    third = "Вася"
elif t >= v and v >= p:
    first = "Толя"
    second = "Вася"
    third = "Петя"
print(' ' * 9, first, ' ' * 9)
print(' ', second)
print(' ' * 17, third)
print(' ' * 3, 'II', ' ' * 6, 'I', ' ' * 6, 'III', sep='')
