from itertools import product, permutations

casts = ["бубен", "пик", "треф", "червей"]
cast, exception = input(), input()
best_cast = [s for s in casts if s.startswith(cast[0:3])][0]
power = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
power.remove(exception)
combine = permutations(product(sorted(power), sorted(casts)), 3)
y = [', '.join(' '.join(j) for j in sorted(i)) for i in combine]
threes = [i for i in y if best_cast in i][:10]
for three in threes:
    print(three)
