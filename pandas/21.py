import pandas as pd
df=pd.read_csv("data.csv")
df["Order_Date"]=pd.to_datetime(df["Order_Date"])
df["Year"]=df["Order_Date"].dt.year
df["Month"]=df["Order_Date"].dt.month
df["Day"]=df["Order_Date"].dt.day
print(df)