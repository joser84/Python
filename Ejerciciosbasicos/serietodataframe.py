import pandas as pd

data =[1,2,3,4,5,67,87,64]

serie=pd.Series(data)

df=serie.to_frame
print(df)