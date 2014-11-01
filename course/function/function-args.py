
def power(x):
	return x * x
print power(5)
print power(15)

def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
print power(2, 13)
print power(2, 14)
#print power(5)
print power(5)

def enroll(name, gender):
	print 'name: ', name
	print 'gender: ', gender
print enroll('Sarah', 'F')

def enroll(name, gender, age = 6, city = 'Beijing'):
	print 'name: ', name
	print 'gender: ', gender
	print 'age: ', age
	print 'city: ', city
print enroll('Michale', 'M')


# 默认参数的坑
def add_end(L=[]):
	L.append('END')
	return L
print add_end([1, 2, 3])
print add_end()
print add_end()
print add_end()

###
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
###
def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L
print add_end()
print add_end()
print add_end()

###
#为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
###

# 可变参数
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print calc([1, 2, 3])
print calc([1, 3, 5, 7])

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print calc(1, 2)
print calc()
nums = [1, 2, 3]
print calc(nums[0], nums[1], nums[2])
#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
print calc(*nums)

# 关键字参数
def person(name, age, **kw):
	print 'name:', name, 'age:', age, 'other:', kw
person('Michael', 30)
person('Bob', 35, city = 'Beijing')
kw = {'city' : 'Beijing', 'job' : 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])
person('Jack', 24, city=kw['city'], job=kw['job'])

# 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
def func(a, b, c = 0, *args, **kw):
	print 'a =', a, 'b=', b, 'c =',c, 'args=', args, 'kw =', kw
func(1, 2)
func(1, 2, c = 3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x = 99)
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)