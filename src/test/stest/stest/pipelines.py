# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from stest.items import StestItem
import json


class StestPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, StestItem):
            line = json.dumps(dict(item)) + "\n"
            with open(mytemp.json, "wb") as f:
                f.write(line)

        return item
