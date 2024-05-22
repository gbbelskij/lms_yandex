class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(name):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_"
    if not isinstance(name, str):
        raise TypeError
    if not all(i in alphabet for i in name):
        raise BadCharacterError
    if name[0] in "1234567890":
        raise StartsWithDigitError
    return name
