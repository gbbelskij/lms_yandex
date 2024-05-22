def recursive_sum(*args):
    if len(args) == 1:
        return args[0]
    return args[-1] + recursive_sum(*(args[:len(args) - 1]))

print(recursive_sum(1, 2, 3 ,4 , 5))
