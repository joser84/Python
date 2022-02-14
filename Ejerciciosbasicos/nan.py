import pandas as pd
import numpy as np
from sqlalchemy import false

data=[1,2,4,'pythom',np.nan]

serie=pd.Series(data)

serie=pd.to_numeric(serie, errors='coerce')
#borrar nan
serie1=serie.dropna()
print(serie1)

#reemplazar nan

serieree=serie.fillna(0,inplace=False)
print(serieree)
