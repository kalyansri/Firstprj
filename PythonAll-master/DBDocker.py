import pymysql
import pdb

# database connection
connection = pymysql.connect(host="localhost", user="root", passwd="password", database="test")

cursor = connection.cursor()

print("Connected")
retrive = "Select * from Persons;"

# executing the quires
cursor.execute(retrive)

rows = cursor.fetchall()
for row in rows:
    print(row)
connection.close()