import pandas as pd

df = pd.read_csv("data.csv")

most_used = df["Payment_Method"].value_counts().idxmax()

print("Most used payment method:",most_used)