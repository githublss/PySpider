#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 获取二次元动漫图片
import requests
from bs4 import BeautifulSoup
import re

sess = requests.Session()
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}


def loadimg(url):
    # url = "https://bcy.net/illust/detail/43286/2048051"
    html = sess.get(url, headers=headers).text  # 获取session
    soup1 = BeautifulSoup(html, "html.parser")
    # detail_std detail_clickable
    # imgs = soup1.findAll('img', {'class': 'detail_std detail_clickable'})
    imgs = soup1.findAll('img', class_= 'detail_std detail_clickable')
    for img in imgs:
        # print img.attrs
        print img['src']

    print '------'


for i in range(1):
    url =("https://bcy.net/u/453458/post/illust?&p=%d"%i)
    html = sess.get(url, headers=headers).text  # 获取session
    soup = BeautifulSoup(html,"html.parser")
    listUrls = soup.findAll('a',href=re.compile('^/illust/detail/'))
    for url in listUrls:
        loadimg("https://bcy.net"+url['href'])