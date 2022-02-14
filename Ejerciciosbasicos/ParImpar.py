import pandas as pd

data =(list(range(10)))

print (data)

serie=pd.Series(data)

#print(serie)

seriepar=serie[serie % 2 == 0]
print (seriepar)

serieimpar=serie[serie % 2 == 1]
print (serieimpar)