import pandas as pd 
df=pd.read_csv("data.csv")
products=df.groupby("Category")["Rating"].min()
feedback=products[products>=3]
print(feedback)