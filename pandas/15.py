import pandas as pd
df = pd.read_csv("data.csv")
category_quantity=df.groupby("Category")["Quantity"].sum()
print(category_quantity)