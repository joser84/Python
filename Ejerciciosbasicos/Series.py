import pandas as pd


datos=[2,3,5,7,11]

serie=pd.Series(datos)

print(serie)

#numero de filas
print(len(serie))
#numero de filas y numero de columnas
print(serie.shape)

dataframe1 = serie.describe()
print("Statistics are: \n")
print(dataframe1)