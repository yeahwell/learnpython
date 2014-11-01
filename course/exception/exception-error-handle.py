# try except finally
try:
	print 'try...'
	r = 10 / 0
	print 'result:', r
except ZeroDivisionError, e:
	print 'except:', e
finally:
	print 'finally...'
print 'END'

# try except1,except2 finally
try:
	print 'try...'
	r = 10 / int('a')
	print 'result:', r
except ValueError, e:
	print 'ValueError:', e
except ZeroDivisionError, e:
	print 'ZeroDivisionError:', e
finally:
	print 'finally...'
print 'END'

# try except else finally
try:
	print 'try...'
	r = 10 / int('a')
	print 'result:', r
except ValueError, e:
	print 'ValueError:', e
except ZeroDivisionError, e:
	print 'ZeroDivisionError:', e
else:
	print 'no error'
finally:
	print 'finally...'
print 'END'

# 第二个except永远也捕获不到
try:
	foo()
except StandardError, e:
	print 'StandardError'
except ValueError, e:
	print 'ValueError'

# 跨多层调用
def foo(s):
	return 10 / int(s)
def bar(s):
	return foo(s) * 2
def main():
	try:
		bar('0')
	except StandardError, e:
		print 'Error'
	finally:
		print 'finally...'

