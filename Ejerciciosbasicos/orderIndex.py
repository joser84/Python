import pandas as pd

datos=[1,2,4,45,6]

indexes=['A','B','C','D','E']

serie=pd.Series(data=datos, index=indexes)


serie=serie.reindex(index=['B','E','C','A','D'])
print(serie)
