from itertools import product, permutations

casts = sorted(["бубен", "пик", "треф", "червей"])
cast = input()
exception = input()
past = input()
best_cast = [s for s in casts if s.startswith(cast[0:3])][0]
power = sorted(["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"])
power.remove(exception)
comb = permutations(product(power, casts), 3)
y = sorted(set([', '.join(' '.join(j) for j in sorted(i)) for i in comb]))
threes = [i for i in y if best_cast in i]
for index, three in enumerate(threes):
    if three == past:
        print(threes[index + 1])
        break
