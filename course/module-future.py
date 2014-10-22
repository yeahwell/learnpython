
# still running on Python 2.7

from __future__ import unicode_literals
from __future__ import division

print isinstance('xxx', unicode)
print isinstance(u'xxx', unicode)
print isinstance('xxx', str)
print isinstance(b'xxx', str)

#Python 3.x中，所有的除法都是精确除法，地板除用//表示
print 10 / 3
print 10.0 / 3
print 10 // 3