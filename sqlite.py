import sqlite3
#connect to the sqlite db
connection=sqlite3.connect("student.db")
#create a cursor object to insert record, create table
cursor=connection.cursor()
# create table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25), SECTION VARCHAR(25))
"""
cursor.execute(table_info)
cursor.execute('''Insert Into STUDENT values('Pratiksha','Data Science','A')''')
cursor.execute('''Insert Into STUDENT values('Swara','Data Science','A')''')
cursor.execute('''Insert Into STUDENT values('Riya','Machine Learning','C')''')
cursor.execute('''Insert Into STUDENT values('Damini','Cloud Engineering','B')''')
cursor.execute('''Insert Into STUDENT values('Ritu','Data Science','D')''')
cursor.execute('''Insert Into STUDENT values('Nita','Data Science','A')''')

#Display all the records
print("The inserted records are:")
data = cursor.execute('''select * from STUDENT''')
for row in data:
    print(row)

#commit your changes in db
connection.commit()
connection.close()