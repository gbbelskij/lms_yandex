friends = {}
s = input()
while s != '':
    friend1, friend2 = list(s.split())
    if friend1 in friends:
        friends[friend1].append(friend2)
    else:
        friends[friend1] = [friend2]
    if friend2 in friends:
        friends[friend2].append(friend1)
    else:
        friends[friend2] = [friend1]
all_friends = sorted(list(friends.keys()))
for i in all_friends:
    friends_set = set()
    for j in friends[i]:
        friends_set.update(set(friends[j]))
    friends_pairs = set()
    friends_pairs.add(i)
    friends_pairs.update(set(friends[i]))
    friends_set.difference_update(friends_pairs)
    friends_set = sorted(list(friends_set))
    print(f"{i}: ", end='')
    print(*friends_set, sep=', ')
