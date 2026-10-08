import pandas as pd
df = pd.read_csv("data.csv")
df["Total_Amount"]=df["Quantity"]*df["Price"]
df["Final_Amount"]=df["Total_Amount"]-(df["Total_Amount"] * df["Discount"] / 100)
city_sales = df.groupby("City")["Final_Amount"].sum()
print(city_sales)