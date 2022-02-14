import pandas as pd


data= list(range(50))

serie=pd.Series(data)

serie=serie.nbytes

print(serie)