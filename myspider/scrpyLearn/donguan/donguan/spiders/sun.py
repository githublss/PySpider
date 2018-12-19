# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from donguan.items import DonguanItem

class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/reply?page=30']

    rules = (
        Rule(LinkExtractor(allow=r'reply\?page=\d+'),follow=True),      # 将满足条件的url提取出来给调度器，进行入栈处理。没有进行页面解析
        Rule(LinkExtractor(allow=r'html/question/\d+/\d+\.shtml'),callback= 'parse_item',follow=True)
    )

    def parse_item(self, response):
        item = DonguanItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        item['title'] = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        # 编号
        item['number'] = item['title'].split(' ')[-1].split(':')[-1]
        # 内容
        content = response.xpath("//div[@class='contentext']/text()").extract()
        if len(content) == 0:
            content = response.xpath("//div[@class='pagecenter p3']//div[@class='c1 text14_2']/text()").extract()
            item['content'] = "".join(content).strip()
        else:
            item['content'] = "".join(content).strip()
        # 链接
        item['url'] = response.url
        yield item
