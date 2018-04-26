# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名称
    positionName = scrapy.Field()
    # 职位类型
    positionType = scrapy.Field()
    # 职位人数
    positionNum = scrapy.Field()
    # 职位区域
    positionArea = scrapy.Field()
    # 职位发布日期
    positionDate = scrapy.Field()
