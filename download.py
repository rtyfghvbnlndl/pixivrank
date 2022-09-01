from datetime import datetime
import os
from time import sleep
import my_fake_useragent as ua
import requests
import get


p1 = ua.UserAgent()
h = {'User-Agent': '%s' % p1.random()}
f = requests.get('https://www.pixiv.net/ranking.php',headers = h)

page_url = get.page_url(f.text)
t = datetime.now()
d = './%s.%s.%s' % (t.year,t.month,t.day)
if not os.path.exists(d):
    os.mkdir(d)
n = 0
for url in page_url:
    n += 1
    print(n,url)
    sleep(4)
    f1= requests.get(url,headers = h)
    img_url = get.img_url(f1.text)
    print(img_url)
    sleep(4)
    f2= requests.get(img_url[0],headers = h)
    from contextlib import closing
    with closing(f2) as response:
        with open('%s/#%i%s.%s' % (d,n,get.title(f1.text)[0],get.pic_name(img_url[0])[0]),'wb') as pic:
            for chunk in response.iter_content(128):
                pic.write(chunk)
                print('finish')
