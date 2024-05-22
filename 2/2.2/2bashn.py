n = int(input())
d1 = n // 100
d2 = n // 10 % 10
d3 = n % 10
maxi = max(d1, d2, d3)
mini = min(d1, d2, d3)
midd = d1 + d2 + d3 - maxi - mini
print(maxi, midd, sep="", end=" ")
if mini != 0:
    print(mini, midd, sep="")
elif midd != 0:
    print(midd, mini, sep="")
else:
    print(maxi, mini, sep="")
