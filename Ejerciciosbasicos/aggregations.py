import pandas as pd
import numpy as np
 
data=[1,2,3,45,656,77,-5,64,11,-324,33]
data1 =[1,1,2,2,3,3,3,3,3,3,5,5,5,5,6,6,7,1]

serie=pd.Series(data)

serieprom=serie.mean() #promedio
print(serieprom)

seriedev=serie.std() #desviacion estandar
print(seriedev)


seriemax=serie.max() #minimo
print(seriemax)

seriemin=serie.min() #maximo
print(seriemin)


serieabs=serie.abs()
print(serieabs)

seriemax1=serie.agg(max) #nativo de python
print(seriemax1)

serienp=serie.agg(np.sin) #nativo de python
print(serienp)


#funcion propia

def cuadrado(x):
    return x*x

print( serie.agg(cuadrado))
  
#conteo de valores 
serievalue =pd.Series(data1)
serievalue =serievalue.value_counts()
print(serievalue)


#comparar dos series
print(serie.equals(serievalue))
