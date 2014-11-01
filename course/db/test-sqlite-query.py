
#导入SQLite驱动:
import sqlite3
conn = sqlite3.connect('test.db')
#创建一个Curson
cursor = conn.cursor()

cursor.execute('select * from user where id=?', '1')
values = cursor.fetchall()
print values
cursor.close()
conn.close()