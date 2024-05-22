import pandas as pd


def length_stats(s):
    s = ''.join(i for i in s if i.isalpha() or i == ' ')
    dict_s = {i.lower(): len(i) for i in s.split()}
    sorted_dict = dict(sorted(dict_s.items()))
    return pd.Series(sorted_dict.values(), index=sorted_dict.keys())


print(length_stats('Мама мыла раму'))
