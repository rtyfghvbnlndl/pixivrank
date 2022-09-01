# pixivrank
下载pixiv排行榜的图片，获取标题、作者等
# module
1.requests
2.my_fake_useragent
pip install <module>
***
## get.py
1.page_url 获取所有的详情页地址
2.thum_url 获取所有的缩略图地址
3.rank_title 所有的标题
4.rank_num 获取排名[#1,#2,#3,#4...]
5.img_url 在详情页（page_url）中获得大图地址 
6.title 在详情页（page_url）中获得标题
7.user_name 在详情页（page_url）中获得画师名字
8.pic_name 由图片地址（img_url）获得图片扩展名
## download.py
用来下载今日排行榜图片的大图，并以标题命名，存在标有日期的文件夹里。
