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


#------------------------------------------------------------------------------------------------------------
#creacion de un dataframa a partir de un diccionario
#------------------------------------------------------------------------------------------------------------
data2={'A':[1,2,3,4,5],'B':[5,4,3,2,1],'C':[6,7,8,9,10]}        

#creacion de un dataframa a partir de un diccionario
indice=['z','x','y','w','t']
df1=pd.DataFrame(data2)
df2=pd.DataFrame(data=data2,index=indice)
df2=df2.loc['z']
print(df1)
print(df2)


#------------------------------------------------------------------------------------------------------------
#obtener nombre de las filas y columnas
#------------------------------------------------------------------------------------------------------------

print(df1.index)
print(df1.columns)