import sqlite3

connection = sqlite3.connect("student.db") #Connect to the sqlite3

cursor = connection.cursor() #Create a cursor object to inser record

#Create a table
table_info=""" 
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),SECTION VARCHAR(25), MARKS INT);
 """

cursor.execute(table_info) #Execute the query

#Insert records

cursor.execute("INSERT INTO STUDENT VALUES('Raj','DS','A',90)")
cursor.execute("INSERT INTO STUDENT VALUES('Rahul','DL','B',80)")
cursor.execute("INSERT INTO STUDENT VALUES('Ravi','DL','B',70)")
cursor.execute("INSERT INTO STUDENT VALUES('Ramesh','DL','A',86)")
cursor.execute("INSERT INTO STUDENT VALUES('Rajesh','DS','A',70)")


#Displau all the records
print("The inserted records are")

data = cursor.execute(''' Select * From STUDENT ''')

for row in data:
    print(row)

#Close the connection
connection.commit()
connection.close()

