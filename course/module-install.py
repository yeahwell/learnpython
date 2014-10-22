
# 安装easy_install
###
#1. 下载ez_setup.py，python ez_setup.py
#2. 请添加C:\Python27\Scripts到环境变量Path
#3. 在pypi.python.org中找到Python Imaging Library，
###

import Image
im = Image.open('test.jpg')
print im.format, im.size, im.mode
#im.thumbnail((200, 100))
#im.save('thumb.png', 'png')

#import mymodule

#默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，
#搜索路径存放在sys模块的path变量中
import sys
print sys.path

# 添加自己的搜索目录
# 直接修改sys.paht。运行时修改，运行结束后失效。
import sys
sys.path.append('/Users/yeahwell/Documents/R')