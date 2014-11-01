
# 这种一边循环一边计算的机制，称为生成器（Generator）
L = [x * x for x in range(10)]
print L
g = (x * x for x in range(10))
print g
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
#print g.next()

g = (x * x for x in range(10))
for n in g:
	print n

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print b
		a, b = b, a + b
		n = n + 1
fib(6)

#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
print fib(6)

####
#这里，最难理解的就是generator和函数的执行流程不一样。
#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
#再次执行时从上次返回的yield语句处继续执行。
####

def odd():
	print 'step1'
	yield 1
	print 'step2'
	yield 3
	print 'step3'
	yield 5
o = odd()
print o.next()
print o.next()
print o.next()
print o.next()
###
#odd不是普通函数，而是generator，
#在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，
#所以，第4次调用next()就报错。
###