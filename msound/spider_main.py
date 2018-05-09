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


import url_manager, html_downloader, html_parser
import config


class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()


    def craw_simple(self, root_url,bad_spider=False):
        html_cont = self.downloader.download(root_url);
        # print(html_cont);
        recommend_json = self.parser.parse(root_url, html_cont)  #通过js得到recommend_json
        ready_down_data=self.parser.get_play_list(recommend_json)  #处理json
        final_data=[];
        for key in ready_down_data:
            final_data.append(self.parser._get_sound_json(key));
        for data in final_data:

            self.downloader.download_mp3(data);
    def crwa_first_search_voice(self):
        search=raw_input("请输入你想要下载的名字...\n")
        data=self.parser._get_search_voice_json(config.GLOBAL_SEARCH_VOCIE+search)
        if data != False:
            self.downloader.download_mp3(data);









if __name__ == "__main__":
    root_url = config.GLOBAL_URL
    # print  time.time();
    obj_spider = SpiderMain()
    obj_spider.craw_simple(root_url)
    # obj_spider.crwa_first_search_voice();