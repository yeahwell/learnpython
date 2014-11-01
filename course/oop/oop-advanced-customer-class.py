
#特殊用途的函数

# __str__ 等同于java的toString()
class Student(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student object (name : %s)' % self.name
	__repr__ = __str__

print Student('Wesley')
s = Student('Michael')
print s

# __iter__ 特殊函数
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1 #初始化两个计数器a，b

	def __iter__(self):
		return self #实例本身就是迭代对象

	def next(self):
		self.a, self.b = self.b, self.a + self.b #计算下一个值
		if self.a > 100000:
			raise StopIteration()
		return self.a

for n in Fib():
	print n

# __getattr__
class Student(object):
	def __init__(self):
		self.name = 'Michael'

s = Student()
print s.name
#print s.score

class Student(object):
	def __getattr__(self, attr):
		if attr == 'age':
			return lambda : 25
		raise AttributeError()
s = Student()
print s.age()

###
#如果要写SDK，给每个URL对应的API都写一个方法，
#那得累死，而且，API一旦改动，SDK也要改。
#利用完全动态的__getattr__，我们可以写出一个链式调用
class Chain(object):
	def __init__(self, path=''):
		self._path = path
	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))
	def __str__(self):
		return self._path
print Chain().status.user.timeline.list

# __call__
#任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
class Student(object):
	def __init__(self, name):
		self.name = name
	def __call__(self):
		print('My name is %s' % self.name)
s = Student('Wesley')
s()

# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的
# 判断一个变量是对象还是函数
print callable(Student("Michael"))
print callable(max)
print callable(None)
print callable('string')







