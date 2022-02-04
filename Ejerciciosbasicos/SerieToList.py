import pandas as pd

data=[2,3,5,7,11]

serie=pd.Series(data)

dataframe1=type(data)
print(dataframe1)

dataframe2=type(serie)
print(dataframe2)

lista =serie.tolist()
dataframe3=type(lista)
print(dataframe3)
print(lista)
