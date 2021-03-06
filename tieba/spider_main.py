#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

# 爬虫调度端

## URL管理器

### 添加新的URL到待爬取集合中
### 判断待添加URL是否在容器中
### 获取待爬取URL
### 判断是否还有待爬取URL
### 将URL从待爬取移动到已爬取

## 网页下载器
### urllib2
### requests

## 网页解析器

### 正则表达式
### html.parser
### BeautifulSoup
### lxml


## 分析目标
### URL格式
### 数据格式
### 网页编码


import url_manager, html_downloader, html_outputer, html_parser
import time
import config
import re;

class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.pn=0;


    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try :
                new_url = self.urls.get_new_url()
                # print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.downloader.collect_img(new_data)
                #爬取词条个数 暂定100个
                if count == 20:
                    break
                count = count + 1
            except:
                print 'craw failed'

        self.downloader.downloadImg()
        self.pn+=50;
        self.craw_next();
    def craw_next(self):
        print 'sleeping'
        time.sleep(10)
        craw_url=config.GLOBAL_URL;
        craw_url = re.sub(r'pn=[\d]', 'pn=%d'% self.pn, craw_url)
        if(self.pn == 200):
            return
        self.craw(craw_url);
        pass
if __name__ == "__main__":
    root_url = config.GLOBAL_URL
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
