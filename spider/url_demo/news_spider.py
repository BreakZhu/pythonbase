import urllib.request as ur
import urllib.error as err

import re

data = ur.urlopen("http://news.sina.com.cn/").read()
# 编码后忽略错误
data2 = data.decode("utf-8", "ignore")
# 筛选新闻链接
pat = 'href="(http://news.sina.com.cn/.*?)"'
allurl = re.compile(pat).findall(data2)
success = 1
fail = 1
for i in range(0, len(allurl)):
    try:
        print("第{}次爬取".format(i))
        this_url = allurl[i]  # parse.quote(
        file = "../urls/{}.html".format(i)
        ur.urlretrieve(this_url, file)
        print("第{}次成功".format(success))
        success += 1
    except err.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        print("失败 {} 次".format(fail))
        fail += 1
