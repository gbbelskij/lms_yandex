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
