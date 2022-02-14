import pandas as pd

serie1=pd.Series([1,2,3,4,5])
serie2=pd.Series([13,25,36,4,51])


DataFrame1=serie1>serie2
print(DataFrame1)
DataFrame2=serie1<serie2
print(DataFrame2)
DataFrame3=serie1==serie2
print(DataFrame3)


menorque=serie1.lt(serie2)
print(menorque)
menoroigualque=serie1.le(serie2)
print(menoroigualque)
igual=serie1.eq(serie2) 
print(igual)
mayorque=serie1.gt(serie2)
print(mayorque)
mayoroigualque=serie1.ge(serie2)
print(mayoroigualque)


seriebetween=serie1.between(2,4)
seriebetweeninc=serie1.between(1,5, inclusive=False)
print(seriebetweeninc)