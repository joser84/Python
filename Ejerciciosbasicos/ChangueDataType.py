import pandas as pd

data=pd.Series([1,2,3,'test',1.22,'1,222'])
dataframe1=pd.to_numeric(data,'coerce')
dataframe2=dataframe1.hasnans

print(dataframe1) 
print(dataframe2)