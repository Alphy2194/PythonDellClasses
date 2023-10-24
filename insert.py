import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(1,'EMOBILIS',7,'WESTLANDS',25000.00)");
conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(2,'SAFARICOM',7,'WESTLANDS',25000.00)");
conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(3,'ORACLE',7,'WESTLANDS',25000.00)");
conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
              VALUES(4,'MICROSOFT',7,'WESTLANDS',25000.00)");

conn.commit()
print("Record created successfully")
conn.close()