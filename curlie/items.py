# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CurlieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    category = scrapy.Field()       # 当前所属目录
    subcategory = scrapy.Field()    # 子目录
    name = scrapy.Field()           #子目录项目名字
    url = scrapy.Field()            #子目录项目url
    sites = scrapy.Field()          #当前网页下的网站
    title = scrapy.Field()          # 网站标题
    site_url = scrapy.Field()       #网站url
    description = scrapy.Field()    #网站概述


