import pandas as pd 
data={"name":["abu","anu","manu","ana"],"age":["2","3","4","5"]}
df=pd.DataFrame(data)
print(df.tail(2))