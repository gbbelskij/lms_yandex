from itertools import *

casts = ['пик', 'треф', 'бубен', 'червей']
people = ['валет', 'дама', 'король', 'туз']
numbers = list(range(2, 11))
no_cast = input()
casts.remove(no_cast)
for i in product(numbers + people, casts):
    print(i[0], i[1])
