#import string
#import numpy as np
#import pandas as pd


#cars = np.loadtxt('SURVEY-2020.csv',dtype=np.dtype,delimiter =';')


with open('.\FlatFile\cars.csv','r') as rf:
        with open('.\FlatFile\cars2.txt','w') as wf:
            for line in rf:
                wf.write(line)

#with open('SURVEY-2020.csv','r') as f:

 #   size_to_Read=10

  #  f_contents=f.content


 #   f_contents =f.read(10)
  #  print(f_contents, end='')

  #  for line in f:
   #     print(line, end='')

#    f_contents = f.readline()
#    print (f_contents, end='')

#f=open('SURVEY-2020.csv','r')
#print(f.mode)
#f.close()



 
