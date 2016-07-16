# -*- coding: utf-8 -*-
#抓取深圳招聘python的公司情况

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector,Selector
from lagoushenzhen.items import LagoushenzhenItem
from scrapy.http import FormRequest,Request
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

    def parse(self, response):
        print '******',response.url
        sel = Selector(response)
        total_page = sel.xpath("//span[@class='pager_not_current']")
        print '************',total_page
        # pass
