
#求绝对值
print abs(100)
print abs(-20)
print abs(12.34)
#print abs(1, 2)
#print abs('a')

#比较函数
print cmp(1, 2)
print cmp(2, 1)
print cmp(3, 3)

#数据类型转换
print int('123')
print int(12.34)
print float('12.34')
print str(1.23)
print unicode(100)
print bool(1)
print bool('')

OTHER_NAME_ABS = abs
print OTHER_NAME_ABS(-1)

#自定义函数
def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x
print my_abs(-20)
#空函数
def nop():
	pass
#参数检查
print my_abs('A')
#print abs('A')
#加上参数类型检查
def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x
print my_abs('A')





