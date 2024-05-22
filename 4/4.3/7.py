def same_type(func):
    def decorated(*args):
        if len({type(item) for item in args}) != 1:
            print("Обнаружены различные типы данных")
            return False
        return func(*args)
    return decorated
