# django comes with SQLite3 as default database
import sqlite3

conn = sqlite3.connect('example.db')
print("Openned database successfully")

# Creating a table
# use a method called execute by calling it
conn.execute('''CREATE TABLE COMPANY1(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')
print("Table created successfully")
conn.close()  # close the connection