'''
import mysql.connector
# connecting to the mysql server
db =mysql.connector.connect(
host="localhost",
user="root",
passwd="password"
'''
import mysql.connector as sql
db=sql.connect(host='localhost',user='root',password='123456',database='school')
mycursor=db.cursor()
mycursor.execute("select version()")
for row in mycursor.fetchall():
    print(row)