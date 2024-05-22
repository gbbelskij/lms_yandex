import hashlib


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def passqord_validation(password, min_length=8, possible_chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError
    if len(password) < min_length:
        raise MinLengthError
    if not all(i in possible_chars for i in password):
        raise PossibleCharError
    if not any(map(at_least_one, password)):
        raise NeedCharError
    return hashlib.sha256(password.encode()).hexdigest()
