from distutils.util import execute
import pandas as pd
import pyodbc

data=pd.read_csv('.\FlatFile\cars.csv')
df=pd.DataFrame(data)

print(df)

server = 'DW-A10169\MSSQLSERVER02' 
database = 'test' 
username = 'pyth' 
password = '123'  
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


#data1=pd.read_sql("select * from person",cnxn)
#print(data1)
cursor.execute("DROP TABLE if exists cars")
#cursor=cnxn.execute("ALTER TABLE person " + "ADD detai1l VARCHAR(20)")
cnxn.commit()

cursor.execute('''
		CREATE TABLE cars (
			car_name nvarchar(50),
			mpg nvarchar(50),
            Cylinders nvarchar(50),
            Displacement nvarchar(50),
            Horsepower nvarchar(10),
            Weight nvarchar(10),
            Acceleration nvarchar(10),
            Model nvarchar(50),
            Origin nvarchar(10)
			)
               ''')
cnxn.commit()


for row in df.itertuples():
    cursor.execute("""
                INSERT INTO cars ( car_name, mpg,Cylinders,Displacement,Horsepower,Weight,Acceleration,Model,Origin)
                VALUES (?,?,?,?,?,?,?,?,?)
                """,
                row,
                row,
                row,
                row,  
                row,
                row,
                row,
                row,
                row                  
                )
cnxn.commit()

cnxn.close()