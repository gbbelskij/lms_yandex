import pandas as pd


def cheque(price_list, **kwargs):
    ans = {}

    ans["product"] = sorted(kwargs)
    ans["price"] = [price_list[i] for i in ans["product"]]
    ans["number"] = [kwargs[i] for i in ans["product"]]

    ans["cost"] = [ans["price"][i] * ans["number"][i] for i in range(len(kwargs))]
    return pd.DataFrame(ans)

products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
print(result)
