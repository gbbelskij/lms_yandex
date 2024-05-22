good = input()
price = int(input())
mass = int(input())
money = int(input())
final = price * mass
change = money - final
print("Чек")
print(f"{good} - {mass}кг - {price}руб/кг")
print(f"Итого: {final}")
print(f"Внесено: {money}")
print(f"Сдача: {change}")
