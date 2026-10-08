import pandas as pd 
df=pd.read_csv("data.csv")
df["Total_Amount"]=df["Quantity"]*df["Price"]
df["Final_Amount"]=df["Total_Amount"]-(df["Total_Amount"]*df["Discount"]/100)
sales=df.groupby("Category")["Final_Amount"].sum()
sales_category=sales.idxmax
heigst_sales=sales.max
print("best performing:",sales_category)
print("heigst_sales:",heigst_sales)