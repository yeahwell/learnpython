import urllib.request
import re
import requests
import json
from bs4 import BeautifulSoup #使用了这个包来解析文件
default_timeout = 100 #定义超时时间

# 此类用了post查询歌曲
class NetEase:
    def __init__(self):
        self.header = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'Referer': 'http://music.163.com/search/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'
        }
        self.cookies = {
            'appver': '1.5.2'
        }
    # 搜索单曲(1)，歌手(100)，专辑(10)，歌单(1000)，用户(1002) *(type)*
    def search(self, s, stype=1, offset=0, total='true', limit=100):
        action = 'http://music.163.com/api/search/get/web'
        data = {
            's': s,
            'type': stype,
            'offset': offset,
            'total': total,
            'limit': limit
        }
        return self.httpRequest('POST', action, data)  
     # song ids --> song urls ( details )
    def songs_detail(self, ids, offset=0):
        tmpids = ids[offset:]
        tmpids = tmpids[0:100]
        tmpids = map(str, tmpids)
        action = 'http://music.163.com/api/song/detail?ids=[' + (',').join(tmpids) + ']'
        try:
            data = self.httpRequest('GET', action)
            return data['songs']
        except:
            return []
    def httpRequest(self, method, action, query=None, urlencoded=None, callback=None, timeout=None):    
        if(method == 'GET'):
            url = action if (query == None) else (action + '?' + query)
            connection = requests.get(url, headers=self.header, timeout=default_timeout)

        elif(method == 'POST'):
            connection = requests.post(
                action,
                data=query,
                headers=self.header,
                timeout=default_timeout
            )

        connection.encoding = "UTF-8"
        connection = json.loads(connection.text)
        return connection
# 根据歌曲id获取评论数量
def getCommentNum(id):
    response = urllib.request.urlopen('http://music.163.com/m/song?id='+str(id))
    # response = urllib.request.urlopen('http://music.163.com/#/search/m/?s=林俊杰&type=1')
    html = response.read()
    respHtml = html.decode("utf8")
    respHtml = respHtml.replace(" ","")
    respHtml = respHtml.replace("\xa9","")
    soup = BeautifulSoup(respHtml, 'html.parser')
    string1 = soup.find(id="cnt_comment_count")
    # string2 = soup.find(attrs={"class":"f-ff2"})
    return (int(string1.string))

###############################################################################

netEase = NetEase()
limit = 100
musics = netEase.search("tfboys",stype=1)
songCount = musics['result']['songCount']
times = int(songCount/limit)+1
songs = dict()
number = 0
passNum = 0
print(songCount)
for y in range(0,times):
    if(y>=times-1) :
        count = songCount%limit
    else:
        count = limit
    offset = limit*y
    if(offset>50):
        offset = offset-passNum
    print(offset)
    print("*")
    musics = netEase.search("tfboys",stype=1,offset=offset,limit=limit)
    passNum = 0
    for x in range(0,count):
        try:
            sondId = musics['result']['songs'][x]['id']
            name = musics['result']['songs'][x]['name'].replace("\u2027","")
            key = name.replace("\u2027","")+"+"+str(sondId)
            commentNum = getCommentNum(sondId)
            songs[key]=commentNum
            print(number)
            print(name)
            number = number+1
        except:
            print('ValueError')
        finally:
            passNum = passNum+1
            pass
print("数据形式为：（'歌曲名+歌曲id'：评论数量）")
res = sorted(songs.items(), key=lambda songs:songs[1], reverse=True)
print(res)
