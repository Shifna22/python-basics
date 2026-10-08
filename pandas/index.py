import pandas as pd

data = pd.Series([10, 20, 30, 40])
result=data[data>20]

print(result)