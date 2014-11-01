
# 装驱动
#$ easy_install mysql-connector-python
#$ easy_install MySQL-python
import mysql.connector

conn = mysql.connector.connect(user='root', password='yeahwell', database='test', use_unicode=True)
cursor = conn.cursor()
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#cursor.execute('insert into user (id, name) values(%s, %s)', ['1', 'Wesley'])
print cursor.rowcount
conn.commit()
cursor.close()

