import pandas as pd

serie1=pd.Series([1,2,3,4,56,4])
serie2=pd.Series([4,62,43,3,0,2])

#resultado de 1*4+2*62+3*43+4*3+4*2 ---producto punto
print(serie1.dot(serie2))

