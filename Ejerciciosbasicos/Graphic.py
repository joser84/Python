import pandas as pd
import matplotlib as mat

datos={"2018":"20","2019":"25","2020":"35","2021":"34","2022":"6"}

serie=pd.Series(datos)

grafico=serie.plot(kind='bar')
print(grafico)