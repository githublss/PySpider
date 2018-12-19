# -*- coding: utf-8 -*-
import scrapy
import os
from sina.items import SinaItem

class SinanewsSpider(scrapy.Spider):
    name = "sinaNews"
    allowed_domains = ["sina.com.cn"]
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        items = []
        # 所有大类的url和标题
        parentTitle = response.xpath("//div[@class='clearfix']/h3/a/text()").extract()
        parentUrls = response.xpath("//div[@class='clearfix']/h3/a/@href").extract()

        # 所有小标题的url和标题
        subTitle = response.xpath("//div[@class='clearfix']/ul/li/a/text()").extract()
        subUrls = response.xpath("//div[@class='clearfix']/ul/li/a/@href").extract()

        # 爬取所有大类
        for i in range(0,len(parentTitle)):
            # 指定目录
            parentFileName = "./data/" + parentTitle[i]
            # 没有目录则创建一个
            if(not os.path.exists(parentFileName)):
                os.makedirs(parentFileName)

            for j in range(0, len(subTitle)):
                item = SinaItem()

                # 保存大类的title和urls
                item['parentTitle'] = parentTitle[i]
                item['parentUrls'] = parentUrls[i]

                if_belong = subUrls[j].startswith(item['parentUrls'])

                if(if_belong):
                    subFilename = parentFileName + '/' + subTitle[j]
                    if(not os.path.exists(subFilename)):
                        os.makedirs(subFilename)

                    # 存储小类的url，title和filename字段数据
                    item['subUrls'] = subUrls[j]
                    item['subTitle'] = subTitle[j]
                    item['subFilename'] = subFilename
                    items.append(item)
        for item in items:
            print item['subUrls']
            yield scrapy.Request(url=item['subUrls'],meta={'meta_1':item},callback=self.second_parse)

    def second_parse(self,response):
        meta_1 = response.meta['meta_1']
        sonUrls = response.xpath('//a/@href').extract()
        # print len(sonUrls)

        items = []
        for i in range(0,len(sonUrls)):
            # 检查每个链接是否以大类url开头，以。shtml结尾，如果是返回True
            if_belong = sonUrls[i].endswith('.shtml') and sonUrls[i].startswith(meta_1['parentUrls'])
            # 如果数据属于本大类，获取字段值放在同一个item下便于传输
            if(if_belong):
                item = SinaItem()
                item['parentTitle'] = meta_1['parentTitle']
                item['parentUrls'] = meta_1['parentUrls']
                item['subTitle'] = meta_1['subTitle']
                item['subUrls'] = meta_1['subUrls']
                item['subFilename'] = meta_1['subFilename']
                item['sonUrls'] = sonUrls[i]
                items.append(item)
        # 发送每个小类下子链接的Request请求，得到response后连同包含meta数据一同交给回调函数detail_parse
        for item in items:
            yield scrapy.Request(url=item['sonUrls'],meta={'meta_2':item},callback=self.detail_parse)
    #数据解析方法,获取文章的标题和内容
    def detail_parse(self,response):
        item = response.meta['meta_2']
        content = ""
        head = response.xpath("//h1[@class='main-title']/text()").extract()
        content_list = response.xpath("//div[@class=\'article\']/p/text()").extract()
        # 将p标签里面的文本内容合并到一起
        for content_one in content_list:
            content+=content_one

        item['head'] = head
        item['content'] = content
        yield item
