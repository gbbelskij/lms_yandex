import pandas as pd


def best(data):
    ans = data.copy()
    for i in range(len(ans)):
        if ans["maths"][i] < 4 or ans["physics"][i] < 4 or ans["computer science"][i] < 4:
            ans.drop(i, inplace=True)
    ans.reset_index(drop=True, inplace=True)
    return ans


columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = best(journal)
print(journal)
print(filtered)
