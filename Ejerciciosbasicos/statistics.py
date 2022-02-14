import pandas as pd

data = (list(range(5)))

print(data)

serie=pd.Series(data)
print(serie)

sere1des=serie.describe()
print(sere1des)
