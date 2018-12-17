import urllib.request as ur
import re

keyword = '短裙'
url = 'http://s.taobao.com/list?' \
      'q={}&cat=16&style=grid&seller_type=taobao&' \
      'spm=a217f.8051907.1000187.1&bcoffset=12&s={}'
ua = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/69.0.3497.81 Safari/537.36")
pic_url = '"picUrl":"(.*?)"'
keyword = ur.quote(keyword)
opener = ur.build_opener()
opener.addheaders = [ua]
ur.install_opener(opener)
for i in range(0, 3):
    url = url.format(keyword, i*60)
    data = ur.urlopen(url).read().decode("utf-8", "ignore")
    img_urls = re.compile(pic_url).findall(data)
    print(img_urls)
    for index in range(0, len(img_urls)):
        img_url = "http:" + img_urls[index]
        img_type = img_url.split('.')[-1]
        f = 'D:\\data\\tao_img\\img_{}_{}.{}'.format(i, index,img_type)
        ur.urlretrieve(img_url, f)
