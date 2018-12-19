#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import urllib
from requests import post
from multiprocessing import Pool
from threading import Thread
def my():
    url = "http://video.wanfangdata.com.cn/acy/voteMobile/X10A05"

    headers = {
    "Host" : "video.wanfangdata.com.cn",
    "Connection" : "keep-alive",
    "Content-Length" : "0",
    "Accept": "application/json, text/plain, */*",
    "Origin" : "http://video.wanfangdata.com.cn",
    "User-Agent" : "Mozilla/5.0 (Linux; Android 4.4.2; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
    "Referer": "http://video.wanfangdata.com.cn/page/ui/vote/",

    "Accept-Language" : "zh-CN,en-US;q=0.8",

    "X-Requested-With" : "com.android.browser",}

    # formdata = {
    # }
    # data = urllib.urlencode(formdata)
    # request = urllib2.Request(url, data=data, headers= headers)
    request = post(url, headers= headers)
    print request.text
def main():
    for i in range(100):
        i = Thread(target=my)
        i.start()
        # print i
if __name__ == '__main__':
        main()