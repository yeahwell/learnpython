# 使用元类
from hello import Hello
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

#type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义
def fn(self, name='world'):
	print('Hello, %s ' % name)
# 创建Hello class
Hello = type('Hello', (object, ), dict(hello=fn))
print(type(Hello))
print(type(h))

'''
要创建一个class对象，type()函数依次传入3个参数：
1. class的名称；
2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''

# metaclass是创建类，所以必须从'type'类派生
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

class MyList(list):
	__metaclass__ = ListMetaclass

L = MyList()
L.add(1)
print L
#l = list()
#print l.add(1)

