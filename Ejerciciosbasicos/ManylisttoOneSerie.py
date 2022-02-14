from turtle import pd
import pandas  as pd
from sqlalchemy import true

data =(['Bogota','Cartagena','N/A'],['Tunja','Barranquilla'],['yopal']) 

serie=pd.Series(data)
print(data)

serie = serie.apply(pd.Series).stack().reset_index(drop=True)

print(serie)