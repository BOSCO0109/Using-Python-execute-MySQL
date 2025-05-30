# Using-Python-execute-MySQL
# Using python executing the mysql

from sqlalchemy import create_engine
import pandas as ps

import mysql.connector

A = mysql.connector.connect(                          #using the mysql to connenct the servor of mysql 
    host = 'localhost',
    user = 'root',             
    password = '########',                           #Hiding the using for privacy 
    database = 'dummy_1' 

)

B = A.cursor()                                      #create the cursor to access 

query = "select * from student where roll_number=6"           #query for output 

B.execute(query)                                    # use the execute function to execute the query from sql database

result = B.fetchall()                                #fetchall is used to fetch all the details also there is (fetchone this will execute only one line)

for i in result:                                      # using for loop to run the function in loop to print all the lines
    print(i)


A.close()                                            #and we close the function 


