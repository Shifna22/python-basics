import pandas as pd 
df=pd.read_csv("data.csv")
df["Order_Date"]=pd.to_datetime(df["Order_Date"])
df["Total_Amount"]=df["Quantity"]*df["Price"]
df["Final_Amount"]=df["Total_Amount"]-(df["Total_Amount"]*df["Discount"]/100)
sales=df.groupby(df["Order_Date"].dt.month)["Final_Amount"].sum()
print(sales)
hiegst=sales.idxmax
print(hiegst)
