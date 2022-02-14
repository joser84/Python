import pandas as pd

serie1=pd.Series([1,2,3,4,5])
serie2=pd.Series([9,8,7,6,4])

dataframe1=serie1+serie2
print(dataframe1)

dataframe2=serie1-serie2
print(dataframe2)

dataframe3=serie1*serie2
print(dataframe3)

dataframe4=serie1/serie2
print(dataframe4)


serie=pd.Series(list(range(1,11)))
serie1=pd.Series(list(range(10,0, -1)))


sum1=serie.add(serie1)
print(sum1)

resta=serie.subtract(serie1)
print(resta)

divi=serie.divide(serie1)
print(divi)

multi=serie.multiply(serie1)
print(multi)