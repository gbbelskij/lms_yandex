s1 = input()
s2 = input()
s3 = input()
array = []
for i in s1, s2, s3:
    if 'зайка' in i:
        array.append(i)
print(max(array), len(max(array)))
