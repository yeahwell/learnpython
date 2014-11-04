
try:
	import cPickle as pickle
except ImportError:
	import pickle

d = dict(name='Bob', age=20, score=88)
#pickle.dumps()方法把任意对象序列化成一个str，
print pickle.dumps(d)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print d

