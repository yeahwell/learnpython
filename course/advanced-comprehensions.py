
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
print range(1, 11)

#生成[1x1, 2x2, 3x3,...,10x10]
#方式1，使用for循环
L= []
for x in range(1, 11):
	L.append(x * x)
print L
#方式2，使用列表生成式
print [ x * x for x in range(1, 11)]

#筛选出仅偶数的平方
print [x * x for x in range(1, 11)  if x % 2 == 0]
#使用两层循环，可以生成全排列
print [m + n for m in 'ABC' for n in 'XYZ']

#列出当前目录下的所有文件和目录名
#导入os模块
import os
#os.listdir可以列出文件和目录
print [d for d in os.listdir('.')]

#for循环其实可以同时使用两个甚至多个变量，比如dict的iteritems()可以同时迭代key和value：
d = {'x': 'A', 'y' : 'B', 'z' : 'C'}
for k, v in d.iteritems():
	print k, '=', v
print [k + '=' + v for k, v in d.iteritems()]

L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]
