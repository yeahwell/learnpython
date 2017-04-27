#!/usr/bin/env python
#coding=utf-8

import os
import gtk
import gobject

from pyinotify import WatchManager, Notifier, ProcessEvent, ThreadNotifier, IN_CREATE, IN_DELETE, IN_MOVED_TO, IN_MOVED_FROM

class hechao(ProcessEvent):
	def process_IN_CREATE(self, event):
		print "创建文件： %s " % os.path.join(event.path, event.name)

	def process_IN_DELETE(self, event):
		print "删除文件： %s " % os.path.join(event.path, event.name)

	def process_IN_MOVED_FROM(self, event):
		print "移来文件： %s " % os.path.join(event.path, event.name)

	def process_IN_MOVED_TO(self, event):
		print "移走文件： %s " % os.path.join(event.path, event.name)

path = "./test"
gobject.threads_init()
wm = WatchManager()
mask = IN_DELETE | IN_CREATE | IN_MOVED_TO | IN_MOVED_FROM
notifier = ThreadNotifier(wm, hechao())
wm.add_watch(path, mask, rec=True)
notifier.start()

def __quit(widget):
	notifier.stop()
	gtk.main_quit()

if __name__ == "__main__":
	win = gtk.Window()
	win.connect("destroy", __quit)
	win.show()
	gtk.main()
