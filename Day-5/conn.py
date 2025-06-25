'''import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',password='123456')
if not db.is_connected():
    print('Cound not connect.')
else:
    print('Connected to MySQL.')
c=db.cursor()
db_str='create database if not exists employee_DB'
c.execute(db_str)
c.execute('use employee_DB')
c.execute('show databases')
for row in c.fetchall():
    print(row)
c.close()
db.close()

import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',password='123456',database='employee_DB')
c=db.cursor()
c.execute('use employee_DB')
tbl_str='''
'''

CREATE TABLE tblemployee (empid INT NOT NULL AUTO_INCREMENT,
    empname VARCHAR(45) NOT NULL,
    department VARCHAR(45) NOT NULL,
    salary INT NULL, PRIMARY KEY (empid))'''
#c.execute(tbl_str)
import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',password='123456',database='employee_DB')
c=db.cursor()
#employeetbl_insert = """INSERT INTO tblemployee (empname,department,salary)VALUES (%s, %s, %s)"""
#data=[('Rajni','HR',60000),('Somya','Sales',50000)]
#c.executemany(employeetbl_insert,data)
#db.commit()
#print('Inserted Successfully')

#update
employeetbl_update = "UPDATE tblemployee SET salary = 115000 WHERE empid = 3"
c.execute(employeetbl_update)
db.commit()
#delete
employeetbl_delete = "DELETE FROM tblemployee WHERE empid = 3"
c.execute(employeetbl_delete)
db.commit()
#select
slc_str='select * from tblemployee'
c.execute(slc_str)
for row in c.fetchall():
    print(row)









