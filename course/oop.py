﻿
#面向过程
std1 = { 'name' : 'Michael', 'score' : 98 }
std2 = { 'name' : 'Bob', 'score' : 81 }

def print_score(std):
	print '%s: %s' % (std['name'], std['score'])

print_score(std1);
print_score(std2);

#面向对象编程
class Student(object):

	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print '%s: %s' % (self.name, self.score)

bart = Student('Bart', 59)
lisa = Student('Lisa', 87)
bart.print_score()
lisa.print_score()


