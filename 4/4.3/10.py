def make_linear(arr):
    res = []
    for item in arr:
        if isinstance(item, list):
            res.extend(make_linear(item))
        else:
            res.append(item)
    return res

print(make_linear([1, 2, [3]]))
