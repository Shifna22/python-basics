import pandas as pd
df = pd.read_csv("data.csv")
df["Total_Amount"] = df["Quantity"] * df["Price"]
print(df)