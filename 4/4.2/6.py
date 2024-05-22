in_stock = {"coffee": 4, "milk": 4, "cream": 0}

def order(*args):
    flag = False
    type_of_coffee = {
        "Эспрессо": [1, 0, 0],
        "Капучино": [1, 3, 0],
        "Макиато": [2, 1, 0],
        "Кофе по-венски": [1, 0, 2],
        "Латте Макиато": [1, 2, 1],
        "Кон Панна": [1, 0, 1],
    }
    for i in args:
        flag = False
        temp = type_of_coffee[i]
        if in_stock["coffee"] - temp[0] < 0 or in_stock["milk"] - temp[1] < 0 or in_stock["cream"] - temp[2] < 0:
            continue
        else:
            flag = True
            in_stock["coffee"] -= temp[0]
            in_stock["milk"] -= temp[1]
            in_stock["cream"] -= temp[2]
            return i
    if not flag:
        return 'К сожалению, не можем предложить Вам напиток'

print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
