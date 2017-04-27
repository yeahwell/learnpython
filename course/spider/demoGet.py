import urllib
import urllib2

values = {"username":"yeahwell19920525@qq.com","password":"yjw19920525"}
data = urllib.urlencode(values) 
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()