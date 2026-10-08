import pandas as pd 
df=pd.read_csv("data.csv")
average=df["Rating"].mean()
df["Rating"]=df["Rating"].fillna(average)
print(df)
