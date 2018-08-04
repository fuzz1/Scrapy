# -*- coding: utf-8 -*-
import scrapy


class PengpaiSpider(scrapy.Spider):
    name = 'pengpai'
    allowed_domains = ['https://www.thepaper.cn/']
    start_urls = ['http://https://www.thepaper.cn//']

    def parse(self, response):
        pass
