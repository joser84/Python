import pandas as pd

ciudades =['bogota','buenos aires','brasilia','ciudad de mexico']
paises =['colombia','argentina','brasil','mexico']

serie=pd.Series(ciudades, index=paises)

diccionario=serie.to_dict()
print (diccionario)
