from datetime import date
import pandas as pd
import pyodbc 



server = 'DW-A10169\MSSQLSERVER02' 
database = 'test' 
username = 'pyth' 
password = '123'  
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
# select 26 rows from SQL table to insert in dataframe.
query = "SELECT Id, [Name] FROM Person;"
#df = pd.read_sql(query, cnxn)
#print(df.head(26))







