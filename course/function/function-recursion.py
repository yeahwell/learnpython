
def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)

print fact(1)
print fact(5)
print fact(100)
# 栈溢出
# print fact(1000)

# 尾递归调用
def fact(n):
	return fact_iter(1, 1, n)

def fact_iter(product, count, max):
	if count > max:
		return product
	return fact_iter(product * count, count + 1, max)

print fact_iter(1, 1, 5)
print fact_iter(1, 2, 5)
print fact_iter(2, 3, 5)
print fact_iter(6, 4, 5)
print fact_iter(24, 5, 5)
print fact_iter(120., 6, 5)

###
#针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
#Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。