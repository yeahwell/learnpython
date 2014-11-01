# 协程，又称微线程，纤程。英文名Coroutine。
# 协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。
import time

def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print('[CONSUMER] Consuming %s...' % n)
		time.sleep(1)
		r = '200 OK'

def produce(c):
	c.next()
	n = 0
	while n < 5:
		n = n + 1
		print('[PRODUCER] Producing %s ...' % n)
		r = c.send(n)
		print('[PRODUCER] Consumer return: %s ' % r)
	c.close()

if __name__ == '__main__':
	c = consumer()
	produce(c)

# 最后套用Donald Knuth的一句话总结协程的特点：
#子程序就是协程的一种特例。