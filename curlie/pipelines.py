# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import json
from scrapy.exceptions import DropItem

class CurliePipeline(object):
    def process_item(self, item, spider):
        return item

# class DuplicatesPipeline(object):
#     #去重
#     def __init__(self):
#         self.category_set = set()
#
#     def process_item(self, item, spider):
#         category = item['category']
#         if category in self.category_set:
#             raise DropItem("Duplicate book found:%s" % item)
#         else:
#             self.category.add(category)
#         return item
# 写入json文件的代码还有错误，self.file.write(content)
# class JsonWritePipeline(object):
#     def __init__(self):
#         self.file = open('curlie.jl', 'wb')
#
#     def process_item(self, item, spider):
#         content = json.dumps(dict(item)) + "\n"
#         self.file.write(content)
#         return item
#
#     def close_spider(self, spider):
#         self.file.close()
