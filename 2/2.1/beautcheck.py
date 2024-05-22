good = input()
price = int(input())
mass = int(input())
money = int(input())
final = price * mass
change = money - final
length = 35
price_str = str(mass) + 'кг * ' + str(price) + 'руб/кг'
space_for_price = ' ' * (length - len(price_str) - len('Цена:'))
print(f"{'Чек' :=^35}")
print(f"Товар:{good: >29}")  # 29 = length - len('Товар:')
print("Цена:" + space_for_price + price_str)
print(f"Итого:{final: >26}руб")  # 29 = length - len('Итого:' + 'руб')
print(f"Внесено:{money: >24}руб")  # 27 = length - len('Внесено: + 'руб')
print(f"Сдача:{change: >26}руб")  # 29 = length - len('Сдача:' + 'руб')
print("=" * 35)
