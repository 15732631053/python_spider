#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import re
import urlparse
import config
from bs4 import BeautifulSoup


class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        img_data=self._get_new_img(page_url,soup);
        return new_urls, new_data,img_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/p/(?!\#).*"))

        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        if page_url == config.GLOBAL_URL:
            return {'url':'','title':'','summary':''};
        res_data['url'] = page_url
        # print page_url;
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('div', class_= "article").find("h1")
        res_data['title'] = title_node.get_text()

        p_node = soup.find('div', class_= "article").find_all('p')
        res_data['summary']='';
        for p in p_node:
            res_data['summary']+= p.get_text()
        return res_data
    def _get_new_img(self, page_url, soup):
        res_data=set()
        if page_url == config.GLOBAL_URL:
            return
        img_node=soup.find('div', class_= "article").find_all('div',class_="image-package");
        for img in img_node:
            imgSrc=img.find('img');
            imgSrc=imgSrc.get('data-original-src');
            if imgSrc:
                #https://upload-images.jianshu.io/upload_images/8298000-57bdbe2259dc0fca.jpg
                imgSrc='https:'+imgSrc;
            res_data.add(imgSrc)
        return res_data;





