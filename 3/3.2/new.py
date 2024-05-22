n = int(input())
all_dishes = set()
used_dishes = set()
for _ in range(n):
    all_dishes.add(input())
m = int(input())
for i in range(m):
    number_dishes = int(input())
    for j in range(number_dishes):
        used_dishes.add(input())
for i in sorted(all_dishes - used_dishes):
    print(i)
