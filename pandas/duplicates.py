import pandas as pd 
df=pd.read_csv("data.csv")
print("duplicates:",df.duplicated().sum())
df=df.drop_duplicates()
print(df)