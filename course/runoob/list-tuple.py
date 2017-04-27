
# list
classmates = ['Michael', 'Bob', 'Tracy']
print classmates
print len(classmates)
print classmates[0],classmates[-1]
classmates.append('Adam')
print classmates
classmates.insert(1, 'Jack')
print classmates
classmates.pop()
print classmates
classmates.pop(1)
print classmates
classmates[1] = 'Sarah'
print classmates

L = ['Apple', 123, True]
print L
s = ['python', 'java', ['asp', 'php'], 'scheme']
print len(s)
L = []
print len(L)

# 元组tuple，tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
print classmates
t = (1, 2)
print t
# 定义一个空的tuple
t = ()
print t
# 定义一个只有1个元素的tuple，错误示范
t = (1)
print t
# 定义一个只有1个元素的tuple，正确示
t = (1, )
# Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。
print t
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t
t[0] = 'haha'
print t