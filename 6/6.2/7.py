import pandas as pd


def need_to_work_better(data):
    ans = data.copy()
    for i in range(len(ans)):
        if ans["maths"][i] != 2 and ans["physics"][i] != 2 and ans["computer science"][i] != 2:
            ans.drop(i, inplace=True)
    return ans


columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = need_to_work_better(journal)
print(journal)
print(filtered)
