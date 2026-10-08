import pandas as pd

df = pd.read_csv("data.csv")

df["Total_Amount"] = df["Quantity"] * df["Price"]

df["Final_Amount"] = df["Total_Amount"] - (
    df["Total_Amount"] * df["Discount"] / 100
)

customer_spending = df.groupby("Customer")["Final_Amount"].sum()

top_customer = customer_spending.idxmax()
highest_spending =customer_spending.max()

print("Customer:", top_customer)
print("Total Spent:", highest_spending)