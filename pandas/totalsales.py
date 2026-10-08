import pandas as pd

df = pd.read_csv("data.csv")
df["Total_Amount"] = df["Quantity"] * df["Price"]

df["Final_Amount"] = df["Total_Amount"] - (
    df["Total_Amount"] * df["Discount"] / 100)
average_order_value = df["Final_Amount"].mean(25)
print(average_order_value)