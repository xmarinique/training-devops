import mysql.connector
import subprocess as sp

data = sp.getoutput('tail -n 1 /home/marinique/Scripts/dummy_data.log')


#establishing the connection
conn = mysql.connector.connect(
   user='root', password='Marinique2022!!', host='localhost', database='marinique')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
sql = "INSERT INTO dummy_data(data) VALUES (%s)"
val = [data]


try:
   # Executing the SQL command
   cursor.execute(sql, val)

   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

print("Data inserted")

# Closing the connection
conn.close()

print("Connection closed")
