import re
from typing import Counter
import requests
import my_fake_useragent as ua


def page_url(source):
    page_url1 = re.findall('''class="ranking-image-item"><a href="(.{8,20})"''',source)
    page_url = []
    for l in page_url1:
        page_url.append('https://www.pixiv.net%s' % l)
    return page_url

def thum_url(source):
    thum_url = re.findall('data-src="(https.{1,100})"data',source)
    return thum_url

def rank_title(source):
    title = re.findall('rel="noopener">(.{1,50})</a></h2>',source)
    return title

def rank_num(source):
    number = re.findall('href="(#\d{1,3})',source)
    return number

def img_url(source):
    url = re.findall('original":"(http.{15,150})"}',source)
    return url

def title(source):
    title = re.findall('''"illustTitle":"(.{1,50})","illustComment''',source)
    return title

def user_name(source):
    name = re.findall(',"userName":"(.{1,50})"},',source)
    return name 

def pic_name(url):
    name = re.findall('\w{3}$',url)
    return name

if __name__ == '__main__':
    p1 = ua.UserAgent()
    h = {'User-Agent': '%s' % p1.random()}
    f = requests.get('https://www.pixiv.net/ranking.php',headers=h)
    print(page_url(f.text),thum_url(f.text),rank_title(f.text),rank_num(f.text))