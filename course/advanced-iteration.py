
#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们成为迭代（Iteration)
d = {'a' : 1, 'b' : 2, 'c' : 3}
for key in d:
	print key

for ch in 'ABC':
	print ch

from collections import Iterable
#str是否可迭代
print isinstance('abc', Iterable)
#list是否可迭代 
print isinstance([1, 2, 3], Iterable) 
#整数是否可迭代
print isinstance(123, Iterable)

#在for循环中同时迭代索引和元素
for i, value in enumerate(['A', 'B', 'C']):
	print i, value

for x, y in [(1, 1), (2, 4), (3, 9)]:
	print x, y

