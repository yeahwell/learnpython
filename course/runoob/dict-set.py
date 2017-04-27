
# dict
d = {'Michale' : 95, 'Bob' : 75, 'Tracy' : 85}
print d['Michale']

d['Adam'] = 67
print d['Adam']
d['Jack'] = 90
print d['Jack']
d['Jack'] = 88
print d['Jack']
# print d['Thomas']
print d.get('Thomas')
print d.get('Thomas', -1)

print 'd =', d
print d.pop('Bob')
print d

# set
s = set([1, 2, 3])
print s
s = set([1, 1, 2, 2, 3, 3])
print s
s.add(4)
print s
s.remove(4)
print s
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2
print s1 | s2

#不可变对象
a = ['c' , 'b', 'a']
a.sort()
print a
a = 'abc'
a.replace('a', 'A')
print a

#所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回
a = 'abc'
b = a.replace('a', 'A')
print b
print a



