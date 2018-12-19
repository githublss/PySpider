# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem
#创建一个爬虫类
class TencentpositionSpider(scrapy.Spider):
    # 爬虫名
    name = "tencentPosition"
    # 允许爬虫的范围
    allowed_domains = ["tencent.com"]
    # 爬虫起始的url
    url = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            # 初始化模型对象
            item = TencentItem()
            # 职位名
            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 职位链接
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['positionNum'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            # 将数据交给管道文件处理
            yield item
        if self.offset <20:
            self.offset += 10


        # 将请求重新发送给调度器入队列，出队列，交给下载器下载
        yield scrapy.Request(self.url + str(self.offset),callback=self.parse)