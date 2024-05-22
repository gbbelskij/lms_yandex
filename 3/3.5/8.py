def f(w1, w2):
    ans = []
    for i in w1:
        if i not in w2:
            ans.append(i)
    return ans


name_file1, name_file2, name_file3 = input(), input(), input()
answer = []
words1 = set()
words2 = set()
with open(name_file1, encoding='utf-8') as file1:
    for i in file1.readlines():
        words1 = words1.union(set(i.split()))

with open(name_file2, encoding='utf-8') as file2:
    for i in file2.readlines():
        words2 = words2.union(set(i.split()))

answer.extend(f(words1, words2))
answer.extend(f(words2, words1))
with open(name_file3, 'w', encoding='utf-8') as file3:
    file3.write('\n'.join(sorted(answer)))
