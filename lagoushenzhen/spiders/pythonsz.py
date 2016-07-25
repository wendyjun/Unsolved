# -*- coding: utf-8 -*-
# 抓取深圳招聘python的公司情况

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector, Selector
from lagoushenzhen.items import LagoushenzhenItem
from scrapy.http import FormRequest, Request
import json
import requests
from bs4 import BeautifulSoup
import pprint


class PythonszSpider(CrawlSpider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com/jobs/list_python?&px=default&city=%E6%B7%B1%E5%9C%B3#filterBox',
    )

    # 获取总页数，并对每页进行遍历
    def parse(self, response):
        print '******', response.url

        data = {
            'first': 'false',
            'pn': '1',
            'kd': 'Python'
        }
        r = requests.post(
            'http://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false',
            data=data
        )
        #把response 转换成字典的形式，然后进行取值
        message_page = json.loads(r.text)
        total_p = message_page['content']['positionResult']['totalCount']

        #确定页码的准确数字
        if  int(total_p) / 15 < float(total_p) / 15:
            cate_p = int(total_p) / 15  + 1
        else:
            cate_p = int(total_p) / 15
            print '**********', total_p, cate_p

        #对每一页以post请求，获得每页字典形式的信息
        for i in range(1,cate_p + 1)[:2]:
            data = {
                'first': 'false',
                'pn': i,
                'kd': 'Python'
            }
            rel = requests.post(
                'http://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false',
                data = data
            )
            cate_message = json.loads(rel.text)
            each_message = cate_message['content']['positionResult']['result']
            # print '*******',each_message

            for j in each_message:



                message = LagoushenzhenItem()
                message['name'] = j['businessZones']['companyFullName']
                print '+++++++++++',message['name']
            # message['company']
            # message['salary']
            # message['time']












        # pass
