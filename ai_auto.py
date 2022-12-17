from urllib.request import urlopen
import scrapy
from AI_auto.items import AiAutoItem
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import itertools

class AI_autoCrawlerSpider(scrapy.Spider):
    
    name = "AI_auto"

    def start_requests(self):
        headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

        for i in range(1,30,10):
            url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&mynews=1&news_office_checked=2829&nso=so:dd,p:all,a:all&start=' + str(i)
            # print('-----------------------------'+'\n', url)
            yield scrapy.Request(url=url, callback=self.crawl_parse,
                                 headers=headers)

    def crawl_parse(self,response):
        page_urls = []
        headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

        for i in range(1,11):
            try:
                page_urls.append(response.xpath(f'//*[@id="sp_nws{i}"]/div/div/a/@href').extract())
            except Exception as e:
                # print(e)
                pass
        print('-----------------------------'+'\n', page_urls)
        for page_url in page_urls:
            for url in page_url:
                # print('-----------------------------'+'\n', url)
                yield scrapy.Request(url=url, callback=self.parse, headers=headers)
    #     for url in page_urls:
    #         # print(url)
    #         yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        item = AiAutoItem()
        item['date'] = response.xpath('//*[@id="article-view"]/div/header/div/article[1]/ul/li[2]/text()').extract()
        item['content'] = response.xpath('//*[@id="article-view-content-div"]/p/text()').getall()
        yield item 
                                    
  