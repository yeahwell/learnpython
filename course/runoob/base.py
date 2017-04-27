# 1.3 数据类型和变量 print absolute value of an integer:
a = 100
if a >= 0:
	print a
else:
	print -a

# 字符串demo
print 'I \'m \"OK\" '
print 'I \'m learning\n Python.'
print '\\\n\\'
print '\\\t\\'
# 用r''表示''内部的字符串默认不转义
print r'\\\t\\'
# Python允许用'''...'''的格式表示多行内容
print '''line1
line2
line3'''

# 布尔值
print True
print False
print 3 > 2
print 3 > 5

# 变量
a = 'ABC'
b = a
a = 'XYZ'
print b

#常量
PI = 3.14159265359
print PI

print 10 / 3
print 10.0 /3
print 10 % 3

# 编码问题
print ord('A')
print chr(65)
print '我是中文1'
u'中'
u'ABC'.encode('utf-8')
u'中午'.encode('utf-8')
