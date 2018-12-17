import urllib.request as ur
import re
import urllib.error

url = "http://blog.csdn.net/"
header = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/69.0.3497.81 Safari/537.36")
opener = ur.build_opener()
opener.addheaders=[header]
ur.install_opener(opener)
data = ur.urlopen(url, timeout=30).read()
mydata = data.decode("utf-8", "ignore")
print(mydata)
pat = 'data-track-view=\'{"mod":"popu_459","con":",(.*?),'
result = re.compile(pat).findall(mydata)
for i in range(0, len(result)):
    f = "../urls/csdn_{}.html".format(i)
    ur.urlretrieve(result[i], f)
    print("第 {} 次抓取成功".format(i+1))
