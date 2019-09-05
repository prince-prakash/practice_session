import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user='root', passwd = '1234',database = 'sakila')
mycur = mydb.cursor()
mycur.execute('Select * from ')

for i in mycur:
    print(i)