
class Student(object):
	pass

bart = Student()
print bart

# 可以自由地给一个实例变量绑定属性
bart.name = 'Bart Simpson'
print bart.name

#__init__方法的第一个参数永远是self，表示创建的实例本身
class Student(object):

	def __init__(self, name, score):
		self.name = name
		self.score = score

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

bart = Student('Bart Simpson', 59)
print bart.name, bart.score
print bart.get_grade()