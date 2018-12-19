#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import re

class Spider:
    def __init__(self):
        self.page = 1
        self.switch = True
    def loadPage(self):
        """
            作用：下载页面
        :return:
        """
        print "正在下载数据....."
        url = "http://www.neihanshequ.com/ "
        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
        request = urllib2.Request(url, headers= headers)
        response = urllib2.urlopen(request)

        html = response.read()
        print html

        pattern = re.compile('<div\sclass="f18 mb20">(.*?)</div>',re.S)

        content_list = pattern.findall(html)

        # self.dealPage(content_list)
    def dealPage(self, content_list):
        """
        处理每页的段子
        :param content_list: 每页段子列表集合
        :return:
        """
        for item in content_list:
            item = item.replace("<p>","").replace("<br>","")
            self.writePage(item)
    def writePage(self, item):
        """
        把每条段子逐个写入文件里
        :param item:
        :return:
        """
        print "正在写入数据...."
        with open("duanzi.txt","a") as f:
            f.write(item)

    def startWork(self):
        """
            控制爬虫运行
        """
        while self.switch:
            self.loadPage()
            command = raw_input("如果继续爬取,请按回车(退出输入quit)")
            if command =="quit":
                self.switch = False
            self.page += 1
        print "谢谢使用!"
if __name__ == "__main__":
    duanziSpider = Spider()
    duanziSpider.loadPage()
    # duanziSpider.startWork()