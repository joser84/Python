from cmath import sqrt
import pandas as pd
import math as mt

serie=pd.Series([11,2,4,656,34],index=['china','alemania','brasil','canada','rusia'])

serielambda=serie.apply(lambda x:x*x)
print(serielambda)



def adicionar_temperatura(x,delta):
    return x+delta
serieadicionartemperatura=serie.apply(adicionar_temperatura,args=(1,))
print(serieadicionartemperatura)


serieraiz=serie.apply(sqrt)
print(serieraiz)