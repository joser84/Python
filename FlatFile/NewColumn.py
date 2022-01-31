from datetime import date
import pandas as pd



data_new = pd.read_csv('.\FlatFile\cars.csv' , usecols=['Car','MPG'], sep=';')
#data_new1 = pd.read_csv('.\FlatFile\SURVEY-2020.csv' , dtype={'Year':object}, usecols=['Year'], sep=',')
#data_new = pd.read_csv('.\FlatFile\cars.csv', dtype={'Car': str,'MPG':str})
data_new1 = pd.read_csv('.\FlatFile\SURVEY-2020.csv' , usecols=['Year'] , sep=',')

##data_new1='2020-01-02'

new_column=data_new1

df=pd.DataFrame(data_new)

#df[['Car','MPG']]

df['new_column']=new_column
data_new.to_csv('.\FlatFile\data_new.csv',index = False)