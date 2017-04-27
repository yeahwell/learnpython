
import urllib2

request = urllib2.Request("http://music.163.com/#/song?id=16426574")
response = urllib2.urlopen(request)
print response.read()