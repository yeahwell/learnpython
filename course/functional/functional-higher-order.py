
###
#高阶函数的定义
#1. 接受函数作为输入
#2. 输出一个函数
###

# 从Python内建的map/reduce函数入手
# map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
def f(x):
	return x * x
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#对一个序列求和
def add(x, y):
	return x + y
print reduce(add, [1, 3, 5, 7, 9])

def fn(x, y):
	return x * 10 + y
print reduce(fn, [1, 3, 5, 7, 9])

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print reduce(fn, map(char2num, '13579'))

def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn, map(char2num, s))

#使用lambda函数简化
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
	return reduce(lambda x,y: x*10+y, map(char2num, s))

# 排序算法
print sorted([36, 5, 12, 9, 21])
# sorted()函数也是一个高阶函数
def resersed_cmp(x, y):
	if x > y:
		return -1
	if x < y:
		return 1
	return 0
#实现倒叙排序
print sorted([36, 5, 12, 9, 21], resersed_cmp)
# 字符串的排序
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
print sorted(['about', 'bob', 'Zoo', 'Credit'])

# 实现忽略大小写的排序
def cmp_ignore_case(s1, s2):
	u1 = s1.upper()
	u2 = s2.upper()
	if u1 < u2:
		return -1
	if u1 > u2:
		return 1
	return 0
print sorted(['about','bob', 'Zoo', 'Credit'], cmp_ignore_case)

#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
#实现一个可变参数的求和
def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax
#需要立刻求和，而是在后面的代码中，根据需要再计算怎么办
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
f = lazy_sum(1, 3, 5, 7, 9)
print f
print f()
###
#在函数lazy_sum中又定义了函数sum，
#并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
#当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
#这种称为“闭包（Closure）”的程序结构拥有极大的威力。
###
#当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1 == f2