import pandas as pd

df = pd.read_csv("data.csv")

df["Total_Amount"] = df["Quantity"] * df["Price"]

df["Final_Amount"] = df["Total_Amount"] - (
    df["Total_Amount"] * df["Discount"] / 100
)

top_5_customers = (
    df.groupby("Customer")["Final_Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print(top_5_customers)