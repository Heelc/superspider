#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

import scrapy
from scrapy.http import Request
from stest.items import StestItem
from bs4 import BeautifulSoup

import sys
reload(sys)

sys.setdefaultencoding('utf8')



class MyTestSpider(scrapy.Spider):
    
    name = 'dingdian'
    allowed_domains = ['23us.so']
    base_url_start = 'https://www.23us.so/list/{0}_1.html'
    
    def start_requests(self):
        for i in range(1, 10):
            url = self.base_url_start.format(i)
            yield Request(url, self.parse)


    def parse(self, response):
        max_num = BeautifulSoup(response.text, 'lxml')\
                .find('div', class_ = 'pagelink')\
                .find_all('a')[-1]\
                .get_text()
        bashurl = str(response.url)[:-7]
        for num in range(1, int(max_num) + 1):
            url = bashurl + '_' + str(num) + '.html'
            yield Request(url, callback = self.get_name)

        print bashurl 
        print max_num 
    
    def get_name(self, response):
        tds = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor='#FFFFFF')

        for td in tds:
            novelname = td.find('a').get_text()
            novelurl = td.find('a')['href']
            yield Request(novelurl, callback = self.get_chapterurl, meta = {
                'name': novelname, 
                'url': novelurl,
                })

    def get_chapterurl(self, response):
        item = StestItem()
        item['name'] = str(response.meta['name']).replace('\xa0', '')
        item['novelurl'] = response.meta['url']
        chaper_soup = BeautifulSoup(response.text, 'lxml')
        category = chaper_soup.find('table').find('a').get_text()
        author = chaper_soup.find('table').find_all('td')[1].get_text()
        bash_url = chaper_soup.find('p', class_ = 'btnlinks')\
                .find('a', class_ = 'read')['href']

        code = str(bash_url)[-6:-1].replace('/', '')
        item['category'] = str(category).replace('/', '')
        item['author'] = str(author).replace('/', '')
        item['code'] = code 

        return item




