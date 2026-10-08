import pandas as pd 
df=pd.read_csv("data.csv")
df["Total_Amount"]=df["Quantity"]*df["Price"]
df["Final_Amount"]=df["Total_Amount"]-(df["Total_Amount"]*df["Discount"]/100)
summary=df.groupby("Category").agg(Total_Quantity=("Quantity","sum"),total_sales=("Final_Amount",sum),Average_Rating=("Rating","mean"),Average_Price=("Price","mean"))
print(summary)