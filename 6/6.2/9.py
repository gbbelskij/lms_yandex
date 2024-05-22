import pandas as pd


a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))
data = pd.read_csv("data.csv")
new_data = data.loc[(data["x"] >= a) & (data["x"] <= c) & (data["y"] <= b) & (data["y"] >= d)]
print(new_data)
