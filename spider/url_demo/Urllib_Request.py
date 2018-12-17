import urllib.request as rq
import re
import urllib.parse as ps
import urllib.error as err

# 打开网页
data = rq.urlopen("https://read.douban.com/provider/all").read()
data = data.decode("utf-8")
print(data)
pat = '<div class="name">(.*?)</div>'
mydata = re.compile(pat).findall(data)
print(mydata)
with open('./1.txt', 'w', newline="") as fl:
    for s in mydata:
        fl.write(s + "\n")

# 将网页下载到本地
rq.urlretrieve(url='https://read.douban.com', filename='./dou_ban.html')
# 清理urlretrieve 产生的缓存
# rq.urlcleanup()

file = rq.urlopen("https://read.douban.com/provider/all", timeout=300)
# 打印网页信息
print(file.info())
# 返回状态码 200 正常
print(file.getcode())
#  获取网址
print(file.geturl())

# Request 的使用
keyword = "python"
# 如果出现中文使用quote处理
keyword = rq.quote(keyword)
url = 'http://www.baidu.com/s?wd=%s' % keyword
r1_url = rq.Request(url=url)
data = rq.urlopen(r1_url, timeout=300).read()
print(data)

# 登陆 post
#
# url = ""
# mylogin = ps.urlencode({
#     "name": "",
#     "password": ""
# }).encode("utf-8")
# req = rq.Request(url, mylogin)
# data = rq.urlopen(req, timeout=30).read()

"""
301 永久性重定向
302 重定向到临时url
304 请求资源未更新
400 非法请求
401 请求未经授权
404 没有页面
500 服务器内部异常
501 服务器不支持请求的功能
URLError  没有状态码 1、没网 2、网址不存在 3、连不上服务器 
        4、触发了httpError子类
HttpError 有状态码
        
"""

URL = "http://blog.csdn.net"
try:
    rq.urlopen(URL)
    print("成功")
except err.URLError as e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)

# 通过ad 伪装浏览器模拟访问
url = "http://blog.csdn.net/john_hongming/article/details/40181451"
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/69.0.3497.81 Safari/537.36")
# opener = rq.build_opener()
# opener.addheaders = [headers]
# data = opener.open(url, 30).read()
# print(data)


def user_proxy(url, proxy_addr):
    print("使用代理ip")
    proxy = rq.ProxyHandler({"http": proxy_addr})
    opener_ = rq.build_opener(proxy, rq.HTTPHandler)
    rq.install_opener(opener_)
    data1 = rq.urlopen(url, timeout=30).read()
    mada1 = data1.decode("utf-8", "ignore")
    return mada1

proxy_addr = "121.49.110.65:8888"
url = "http://www.baidu.com"
s = user_proxy(url, proxy_addr)
print(len(s))