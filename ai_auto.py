from urllib.request import urlopen
import scrapy
from AI_auto.items import AiAutoItem
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import itertools
import datetime


class AI_autoCrawlerSpider(scrapy.Spider):
    
    name = "AI_auto"

    def start_requests(self):
        headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

        
        press_lists = [2829,1014]
        urls = []
        for press_list in press_lists:
            for term in range(0,30):
                date = (datetime.date(2022, 11,20) + datetime.timedelta(+term)).strftime('%Y%m%d')
                try: 
                    url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&mynews=1&news_office_checked={press_list}&nso=so:dd,p:from{date}to{date}'
                    urls.append([url,press_list])
                except Exception as e:
                    # print(e)
                    pass


        for url, press_list in urls:
            for i in range(1,30,10):
                page_url = url + '&start=' + str(i)
                print('-----------------------------'+'\n', page_url)             
            yield scrapy.Request(url=url, meta = {'press_list': press_list}, callback=self.crawl_parse,
                                headers=headers)

    # def page_parse(self,response):
    #     headers= {
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    #     temp = response.url +'&page=10'
    #     print(temp)
    #     response_temp = requests.get(temp,headers=headers)
    #     soup = BeautifulSoup(response_temp.text, 'html.parser')
    #     end_pages = soup.select('.paging strong')[0].text
    #     for end_page in range(1,int(end_pages)+1):
    #         press_num = response.meta['press_list']
    #         yield scrapy.Request(url=response.url+'&page='+str(end_page), meta = {'press_list': press_num}, callback=self.crawl_parse, headers=headers)



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
        # print('-----------------------------'+'\n', page_urls)
        for page_url in page_urls:
            for url in page_url:
                # print('-----------------------------'+'\n', url)
                press_num = response.meta['press_list']
                yield scrapy.Request(url=url, meta = {'press_list': press_num}, callback=self.parse, headers=headers)
    #     for url in page_urls:
    #         # print(url)
    #         yield scrapy.Request(url=url, callback=self.parse, headers=headers)


    def parse(self, response):
        item = AiAutoItem()
        if response.meta['press_list'] == 2829:
            item['date'] = response.xpath('//*[@id="article-view"]/div/header/div/article[1]/ul/li[2]/text()').extract()
            item['content'] = response.xpath('//*[@id="article-view-content-div"]/p/text()').getall()
            yield item

        elif response.meta['press_list'] == 1014:
            item['press'] = response.xpath('//*[@id="root"]/div[5]/div/div[2]/em[1]/text()').extract()
            item['date'] = response.xpath('//*[@id="root"]/div[5]/div/div[2]/em[2]/text()').extract()
            item['content'] = response.xpath('//*[@id="article_content"]/text()').extract()
            yield item 

