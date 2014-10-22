
# 偏函数
print int('12345')
print int('12345', base=8)
print int('12345', 16)

def int2(x, base=2):
	return int(x,base)
print int2('1000000')
print int2('1010101')

#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int2 = functools.partial(int, base = 2)
print int2('1000000')
print int2('1010101')
print int2('1000000', base = 10)
#创建偏函数时，要从右到左固定参数
#
#
