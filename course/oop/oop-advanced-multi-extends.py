
# 多继承，Mixin
# 多进程的TCP服务
class MyTCPServer(TCPServer, ForkingMixin):
	pass
# 多线程的UDP服务
class MyUDPServer(UDPServer, ThreadingMixin):
	pass
# 
class MyTCPServer (TCPServer, CoroutineMixin):
	pass

