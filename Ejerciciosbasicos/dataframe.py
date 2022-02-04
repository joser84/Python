import pandas as pd

data1 = {'Column A':[1,2,3,4,'test']
        ,'Column B':[3,'prueba',4,5,6]
        ,'Column C':[3,'prueba22',5656.4,5,'test12'] }

df=pd.DataFrame(data1)
#extraer una o mas columnas de un arreglo
columname=df.iloc[:, lambda df:[1,2]]

#extraer un fila de un arreglo
row1=df.iloc[2,:]

print(columname)
print(row1)
print(type(columname)) 