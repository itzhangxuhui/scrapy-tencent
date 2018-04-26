# -*- coding: utf-8 -*-
import scrapy
from zhang.items import ZhangItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):

        # print(response.body)
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        items = []
        for node in node_list:
            item = ZhangItem()
            positionName = node.xpath("./td[1]/a/text()").extract()[0]

            if len(node.xpath("./td[2]/text()")):
                positionType = node.xpath("./td[2]/text()").extract()[0]
            else:
                positionType = ''
            positionNum = node.xpath("./td[3]/text()").extract()[0]
            positionArea = node.xpath("./td[4]/text()").extract()[0]
            positionDate = node.xpath("./td[5]/text()").extract()[0]


            item['positionNum'] = positionNum
            item['positionArea'] = positionArea
            item['positionDate'] = positionDate
            item['positionName'] = positionName
            item['positionType'] = positionType
            yield item
            items.append(item)
        # return items
        if   not  len(response.xpath("//a[@id='next' and @class='noactive']")):
            url = "https://hr.tencent.com/"+response.xpath("//a[@id='next']/@href").extract()[0]
            yield scrapy.Request(url,self.parse)









