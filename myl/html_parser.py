#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/\?p=(\d)*"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls


    def _get_new_data(self, page_url, soup):
        res_data = {};
        # url
        matchObj = re.search(r'paged', page_url, re.M | re.I)
        if matchObj:
            return {'url': '', 'title': '', 'summary': ''};
        res_data['url']=page_url;
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        #https://imgsa.baidu.com/forum/w%3D580/sign=e836957e41ed2e73fce98624b700a16d/ed5dfcca7bcb0a462c53f1c36063f6246a60af02.jpg
        title_node = soup.find('h2', class_= "entry-name").find('a');
        title=title_node.get('title');
        res_data['title'] = title;
        s_node=soup.find('div',class_='entry-content');
        summary=s_node.get_text();
        res_data['summary'] = summary;
        return res_data;

