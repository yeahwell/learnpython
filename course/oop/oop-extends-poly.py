
''' 封装demo'''
class Animal(object):
	def run(self):
		print 'Animal is running...'

class Dog(Animal):
	def run(self):
		print 'Dog is running...'
	def eat(self):
		print 'Eating meat...'

class Cat(Animal):
	def run(self):
		print 'Cat is running...'

dog = Dog()
dog.run()

cat = Cat()
cat.run()

'''多态 demo'''
a = list()
b = Animal()
c = Dog()

print isinstance(a, list)
print isinstance(b, Animal)
print isinstance(c, Dog)

#在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类
print isinstance(c, Animal)

print isinstance(b, Dog)


def run_twice(animal):
	animal.run()
	animal.run()

print run_twice(Animal())
print run_twice(Dog())
print run_twice(Cat())


#调用方只管调用，不管细节，
#而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。
#这就是著名的“开闭”原则：
class Tortoise(Animal):
	def run(self):
		print 'Tortoise is running slowly...'

print run_twice(Tortoise())


#  获取对象的信息
print type(123)
print type('src')
print type(None)
print type(abs)
print type(b)


# type返回type类型
print type(123)==type(456)
print type('abc') == type('123')
print type('abc') == type(123)

import types
print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType
print type([]) == types.ListType
# 所有类型本身的类型就是TypeType
print type(str) == types.TypeType

a = Animal()
d = Dog()
t = Tortoise()
print isinstance(t, Tortoise)
print isinstance(t, Animal)

#能用type()判断的基本类型也可以用isinstance()判断的基本类型也可以用isinstance
print isinstance('a', str)
print isinstance(u'a', unicode)
print isinstance('a', unicode)

print isinstance('a', (str, unicode))
print isinstance(u'a', (str, unicode))
print isinstance(u'a', basestring)

