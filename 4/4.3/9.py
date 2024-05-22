def cycle(iterable):
    temp = []
    for elem in iterable:
        yield elem
        temp.append(elem)
    while temp:
        for elem in temp:
            yield elem
