import pandas as pd

data = list(range(20))

print (data)

serie=pd.Series(data)

arreglo=serie.values
print(arreglo)

print(type(arreglo))