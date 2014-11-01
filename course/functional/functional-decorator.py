
#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
	print '2013-12-25'
f = now
f()

#函数对象有一个__name__属性，可以拿到函数的名字
print now.__name__
print f.__name__

#假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#本质上，decorator就是一个返回函数的高阶函数

def log(func):
	def wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)
	return wrapper

@log
def now():
	print "2014-10-22"
now()

#把@log放到now()函数的定义处，相当于执行了语句：
#now = log(now)

def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print '%s %s():' % (text, func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print '2014-10-22'
now()

##
#和两层嵌套的decorator相比，3层嵌套的效果是这样的：
#now = log('execute')(now)

print now.__name__ #返回wrapper

import functools

def log(fuc):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)
	return wrapper

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print '%s %s():' % (text, func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator

