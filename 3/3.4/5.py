from itertools import *

list1 = list(input().split(', '))
list2 = list(input().split(', '))
list3 = list(input().split(', '))
for i in enumerate(sorted(set(chain(list1, list2, list3))), 1):
    print(f"{i[0]}. {i[1]}")
