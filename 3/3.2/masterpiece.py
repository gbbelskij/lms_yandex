n = int(input())
products = set()
result = []
for _ in range (n):
    products.add(input())
m = int(input())
for _ in range(m):
    recipe = input()
    recipe_products = int(input())
    flag1 = True  # флаг, хватает ли продуктов
    for i in range(recipe_products):
        product = input()
        if product not in products:
            flag1 = False
            break
    if flag1:
        result.append(recipe)
flag2 = False  # флаг, есть ли что приготовить
for i in sorted(result):
    print(i)
    flag2 = True
if not flag2:
    print('Готовить нечего')
