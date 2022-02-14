import pandas as pd

data = [0,1,2,3,4,5,0,6,7,8,9,10,0,0,0]
data1 =list(range(1,45))
data2={'enero':10,'febrero':11,'marzo':12,'mayo':17}
n= 6

serie=pd.Series(data,name='valores')

#print(serie)
serie_nueva=serie[serie == n]

print(serie_nueva)

serie1=pd.Series(data1)
#serie1=serie1.where(serie1==35,'no aplica') reemplazar un valor 
serie1=serie1.where(serie1>=35).dropna() #filtrar un valor 

print(serie1)

#quitar duplicados
print(serie.drop_duplicates())
#como manterner el ultimo registro duplicado de cada valor
print(serie.drop_duplicates(keep='last'))

#filtrar informacion 
seriefilter=pd.Series(data2)
seriefilter=seriefilter.filter(like='e')
seriefilter=seriefilter.filter(regex='^e')

print(seriefilter)

