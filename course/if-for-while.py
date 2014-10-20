# if判断语句
age = 20
if age >= 18:
	print 'your age is', age
	print 'adult'

age = 3
if age >= 18:
	print 'your age is', age
	print 'adult'
else:
	print 'your age is', age
	print 'teenage'

age = 3
if age >= 18:
	print 'adult'
elif age >= 16:
	print 'teenage'
else:
	print 'kid'

age = 20
if age >= 6:
	print 'teenager'
elif age >= 18:
	print 'adult'
else:
	print 'kid'

# for循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
	print name
sum = 0
for x in range(101):
	sum = sum + x
print sum
# while循环
sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print sum

# 输入1982，结果显示00后
# 从raw_input()读取的内容永远以字符串的形式返回，把字符串和整数比较就不会得到期待的结果，必须先用int()把字符串转换为我们想要的整型：
birth = raw_input('birth: ')
if birth < 2000:
	print '00 before'
else:
	print '00 after'

birth = int(raw_input('birth: '))
if birth < 2000:
	print '00 before'
else:
	print '00 after'