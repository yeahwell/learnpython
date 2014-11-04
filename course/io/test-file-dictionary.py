
import os
print os.name
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。、

#获取详细的系统信息
#print os.uname()
print os.environ
print os.getenv('PATH')

#操作文件和目录
print os.path.abspath('.')
print os.path.join(os.path.abspath('.'), 'testdir')
#os.mkdir(os.path.join(os.path.abspath('.'), 'testdir'))
#os.rmdir(os.path.join(os.path.abspath('.'), 'testdir'))

print os.path.split('test.txt')
print os.path.splitext('test.txt')

#os.rename('test.txt', 'test.py')
#os.remove('test.py')

#列出当前目录下的所有目录
print [x for x in os.listdir('.') if os.path.isdir(x)]
#列出所有的.py文件
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']


