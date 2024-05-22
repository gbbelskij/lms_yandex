import pandas as pd
import numpy as np


def length_stats(s):
    s = ''.join(i for i in s if i.isalpha() or i == ' ')
    dict_1 = {i.lower(): len(i) for i in s.split() if len(i) % 2 == 1}
    dict_2 = {i.lower(): len(i) for i in s.split() if len(i) % 2 == 0}
    if all(len(i) > 0 for i in (dict_1, dict_2)):
        return (
            pd.Series(dict(sorted(dict_1.items())).values(), index=dict(sorted(dict_1.items())).keys(), dtype=np.int64),
            pd.Series(dict(sorted(dict_2.items())).values(), index=dict(sorted(dict_2.items())).keys(), dtype=np.int64)
        )
    if len(dict_1) == 0:
        return (
            pd.Series([], dtype=np.int64),
            pd.Series(dict(sorted(dict_2.items())).values(), index=dict(sorted(dict_2.items())).keys(), dtype=np.int64)
        )
    return (
        pd.Series(dict(sorted(dict_1.items())).values(), index=dict(sorted(dict_1.items())).keys(), dtype=np.int64),
        pd.Series([], dtype=np.int64)
    )

odd, even = length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.')
print(odd)
print(even)
