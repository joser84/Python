import pandas as pd

serie1=pd.Series([1,2,3,4,5])
serie2=pd.Series([13,25,36,4,51])


DataFrame1=serie1>serie2
print(DataFrame1)
DataFrame2=serie1<serie2
print(DataFrame2)
DataFrame3=serie1==serie2
print(DataFrame3)
