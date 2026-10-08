import pandas as pd 
data={"name":["abu",None,"manu","ana"],"age":["2",None,"2","5"]}
df=pd.DataFrame(data)
print(df.isnull().sum())
