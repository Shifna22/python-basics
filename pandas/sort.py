import pandas as pd 
df=pd.read_csv("data.csv")
df["Total_Amount"]=df["Quantity"]*df["Price"]
df["Final_Amount"]=df["Total_Amount"]-(df["Total_Amount"]*df["Discount"]/100)
df=df.sort_values("Final_Amount",ascending=False)
print(df)