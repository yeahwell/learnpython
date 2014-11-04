
#读文件
#由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
try:
	f = open('test.txt', 'r')
	print f.read()
finally:
	if f:
		f.close()

#Python引入了with语句来自动帮我们调用close()方法：
with open('test.txt', 'r') as f:
	print f.read()

with open('test.txt', 'r') as f:
	for line in f.readlines():
		print(line.strip()) #把末尾的'\n'删掉

#读二进制文件
#f = open('test.jpg', 'rb')
#print f.read()

#f = open('gbk.txt', 'rb')
#u = f.read().decode('gb2312')
#u
#print u

with open('test.txt', 'w') as f:
	f.write('wesley')
