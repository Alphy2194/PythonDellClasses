import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("DELETE FROM COMPANY1 where ID = 2")
conn.commit()

cursor = conn.execute("SELECT Id, name, age, address, salary FROM COMPANY1")

for row in cursor:
    print("ID =", row[0])
    print("NAME=", row[1])
    print("AGE =", row[2])
    print("ADDRESS =", row[3])
    print("SALARY =", row[4])

print("Operation done successfully")
conn.close()