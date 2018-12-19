#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import lxml
def loadPage(url):
    """
        作用:根据url发送请求,获取服务器响应文件
        url: 需要爬取的url地址
    """
    print "正在下载..."
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

    request = urllib2.Request(url, headers=headers)
    html = urllib2.urlopen(request).read()
    #解析HTML文档为HTML DOM模型
    content = lxml.etree.HTML(html)
    # link_list = content.xpath('//*[@id="thread_top_list"]/li[1]/div/div[2]/div')
    link_list = content.xpath('//*[@class="t_con cleafix"]/div/div/div/a/@href')

    for link in link_list:
        fulllink = "http://tieba.baidu.com" + link
        print fulllink
        # loadImage(fulllink)
def loadImage(link):
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
    request = urllib2.Request(link,headers=headers)
    html = urllib2.urlopen(request).read()
    content = lxml.etree.HTML(html)
    #返回帖子里的所有的图片链接的列表集合
    link_list = content.xpath('//img[@class="BDE_Image"]/@src')
    for link in link_list:
        writeImage(link)
def writeImage(link):
    """
    将html内容写入本地
    :param html: 写入本地的内容,
    """
    # print "正在保存" + filename
    #文件写入
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
    request = urllib2.Request(link, headers=headers)
    image = urllib2.urlopen(request).read()
    filename = link[-10:]
    with open(filename.decode('utf-8'), "ab") as f:
        f.write(image)
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
        loadPage(fullurl)
    print "Thank you used"

if __name__ == "__main__":
    kw = raw_input("请输入需要爬取的贴吧名:")
    beginPage = int(raw_input("请输入要爬取的首页:"))
    endPage = int(raw_input("请输入爬取的最后一页:"))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage)