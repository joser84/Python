from numpy import append
import pandas as pd


data =('java','.net','sql')

serie=pd.Series(data)

serie=serie.append(pd.Series(['javascript']))

print(serie)

