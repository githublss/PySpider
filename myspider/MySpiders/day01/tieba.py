#!/usr/bin/env python
# -*- coding:utf-8 -*-
#**********************************写文件的问题没有解决

import urllib
import urllib2

def loadPage(url, filename):
    """
        作用:根据url发送请求,获取服务器响应文件
        url: 需要爬取的url地址
    """
    print "正在下载" + filename
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

    request = urllib2.Request(url, headers=headers)
    return urllib2.urlopen(request).read()


def writePage(html, filename):
    """
    将html内容写入本地
    :param html: 写入本地的内容,
    """
    filename = str(filename)
    print "正在保存" + filename
    #文件写入
    with open(filename.decode('utf-8'), "a") as f:
        f.write(html)
    # f = open(filename, 'a')
    # f.write(html)
    # f.close()
    print "-" * 30

def tiebaSpider(url, beginPage, endPage):
    """
    贴吧爬虫调度器,负责组合处理每一个页面的url
    :param url: 贴吧url的前部分
    :param beginPage: 起始页
    :param endPage: 结束页
    :return:
    """
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        filename = '第' + str(page) + "页.html"
        fullurl = url + "&pn=" +str(pn)
        # print fullurl
        html = loadPage(fullurl, filename)
        writePage(html, filename)
    print "Thank you used"

if __name__ == "__main__":
    kw = raw_input("请输入需要爬取的贴吧名:")
    beginPage = int(raw_input("请输入要爬取的首页:"))
    endPage = int(raw_input("请输入爬取的最后一页:"))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage)