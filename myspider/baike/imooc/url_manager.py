#!/usr/bin/env python
# -*- coding:utf-8 -*-


# url管理器
### 添加新的URL到待爬取集合中
### 判断待添加URL是否在容器中
### 获取待爬取URL
### 判断是否还有待爬取URL
### 将URL从待爬取移动到已爬取
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 可能会有错
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for url in new_urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
