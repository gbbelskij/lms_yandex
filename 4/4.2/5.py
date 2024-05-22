def to_string(*args, sep=' ', end='\n'):
    result = sep.join(str(i) for i in args)
    result += end
    return result

data = [7, 3, 1, "hello", (1, 2, 3)]
print(to_string(*data, sep=", ", end="!"))
