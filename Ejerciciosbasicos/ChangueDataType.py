import pandas as pd

data=pd.Series([1,2,3,'test',1.22,'1,222'])
dataframe1=pd.to_numeric(data,'coerce')
print(dataframe1) 
