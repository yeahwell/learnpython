
# 装驱动
#$ easy_install mysql-connector-python
#$ easy_install MySQL-python
import mysql.connector

conn = mysql.connector.connect(user='root', password='yeahwell', database='test', use_unicode=True)
cursor = conn.cursor()
cursor.execute('select * from user where id = %s' % '1')
values = cursor.fetchall()
print values
cursor.close()
conn.close()