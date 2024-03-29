# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"
        data = {
            "email": "18854889585",
            "password": "1234567890"
        }
        request = scrapy.FormRequest(url=url,formdata=data,callback=self.parse_page)
        yield request


    # def parse_page(self, response):
    #     with open("renren.html","w",encoding="utf-8") as fp:
    #         fp.write(response.text)

    def parse_page(self, response):
        request = scrapy.FormRequest(url="http://www.renren.com/259452569/profile",
                                     callback=self.parse_profile)
        yield request

    def parse_profile(self, response):
        with open("huge.html","w",encoding="utf-8") as fp:
            fp.write(response.text)
