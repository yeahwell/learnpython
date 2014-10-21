
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print [L[0], L[1], L[2]]

r = []
n = 3
for i in range(n):
	r.append(L[i])
print r

#slice功能
print L[:3]
print L[1:3]
print L[-2:]

L = range(100)
print L[:10]
print L[-10:]
print L[10:20]
#前10个数，每两个取一个
print L[:10:2]
#所有数，每5个取一个
print L[::5]
print L[:]

#tuple也可以用切片操作，只是操作的结果仍是tuple
print (0,1,2,3,4,5)[:3]

#符串也可以用切片操作，只是操作结果仍是字符串
print 'ABCDEFG'[:3]
print 'ABCDEFG'[::2]