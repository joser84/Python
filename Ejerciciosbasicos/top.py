import pandas as pd

data = list(range(1,1000))

serie=pd.Series(data)

seriehead=serie.head(5)
print(seriehead)

serietail=serie.tail(5)
print(serietail)
