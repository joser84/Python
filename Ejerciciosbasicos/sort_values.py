import pandas as pd



data=(1,2322,234,4,33,123)

serie=pd.Series(data)

serie=pd.Series(serie).sort_values()

print(serie)