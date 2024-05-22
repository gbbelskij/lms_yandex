def secret_replace(string: str, **kwargs) -> str:
    ind = 0
    for key, value in kwargs.items():
        ind = 0
        while key in string:
            ind = ind % (len(value))
            string = string.replace(key, value[ind], 1)
            ind += 1
    return string

print(secret_replace("ABRA-KADABRA",
    A=("Z", "1", "!"),
    B=("3",),
    R=("X", "7"),
    K=("G", "H"),
    D=("0", "2"),))
