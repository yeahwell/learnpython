
# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数
print dir('ABC')


print len('ABC')
print 'ABC'.__len__()

class MyObject(object):
	def __len__(self):
		return 100

obj = MyObject()
print len(obj)

print 'ABC'.lower()

class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

obj = MyObject()
#有属性'x'吗
print hasattr(obj, 'x')
print obj.x
#有属性y吗
print hasattr(obj, 'y')
setattr(obj, 'y', 19)
print hasattr(obj, 'y')
print getattr(obj, 'y')
print obj.y

#getattr(obj, 'z')
#获取属性'z'，如果不存在，则返回默认值
print getattr(object, 'z', 404)

print hasattr(obj, 'power')
print getattr(obj, 'power')
fn = getattr(obj, 'power')
print fn
print fn()