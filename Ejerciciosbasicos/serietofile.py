import pandas as pd
from sqlalchemy import false

data=['tunja','bogota','medellin','santander']
data1={"tunja":"1","bogota":"2","medellin":"43","santander":"5"}

serie=pd.Series(data)
serie1=pd.Series(data1, name="valor")


#print(serie.to_csv())


serie1.to_excel('C:/Users/samuelrr.DIGITALWARE/Documents/bi/Python/Ejerciciosbasicos/serietofile.xlsx',engine='xlsxwriter')

