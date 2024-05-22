class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name) -> str:
    alhabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if not isinstance(name, str):
        raise TypeError
    if not all([i.lower() in alhabet for i in name]):
        raise CyrillicError
    if not name.istitle():
        raise CapitalError
    return name


def username_validation(name):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_"
    if not isinstance(name, str):
        raise TypeError
    if not all(i in alphabet for i in name):
        raise BadCharacterError
    if name[0] in "1234567890":
        raise StartsWithDigitError
    return name


def user_validation(**kwargs):
    if len(kwargs) != 3 or not all(i == 'first_name' or i == 'last_name' or i == 'username' for i in kwargs):
        raise KeyError
    if not all(isinstance(i, str) for i in kwargs):
        raise TypeError
    name_validation(kwargs['last_name'])
    name_validation(kwargs['first_name'])
    username_validation(kwargs['username'])
    return kwargs

print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45"))
