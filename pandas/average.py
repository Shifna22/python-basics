import pandas as pd
df=pd.read_csv("data.csv")
result=df.groupby("Category")["Rating"].mean()
print(result)