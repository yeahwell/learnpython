import logging

#如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
def foo(s):
	return 10 / int(s)
def bar(s):
	return foo(s) * 2
def main():
	try:
		bar('0')
	except StandardError, e:
		logging.exception(e)
main()
print 'END'

class FooError(StandError):
	pass
def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' % s)
	raise 10 / n