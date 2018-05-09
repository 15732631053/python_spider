#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import re
import urlparse
import config
from bs4 import BeautifulSoup
import requests
import urllib2
import json
try:
    import cookielib
except:
    import http.cookiejar as cookielib

class HtmlParser(object):

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        }
        self.session = requests.session()
        # 生成github_cookie文件
        self.session.cookies = cookielib.LWPCookieJar(filename='mobo_cookie')

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        recommend_json = self._get_recommend_json(page_url, soup)
        return recommend_json

    def _get_recommend_json(self, page_url, soup):
        response = self.session.get(page_url, headers=self.headers)
        # print response.text;
        # matchObj = re.search(r'(homepage_data(.*)\.json)', response.text, re.M | re.I);
        # print matchObj.group();
        # jsonURL='http://static.missevan.com/home/sounds/201804/14/'+matchObj.group(1);
        jsonURL='http://static.missevan.com/home/sounds/201702/17/recommend_58a6d0a93a4cb.json';
        # print( jsonURL)
        html = urllib2.urlopen(r'%s' % jsonURL)
        #
        hjson = json.loads(html.read())
        return   hjson['sounds'];
        # return new_full_url
    def get_play_list(self,urllist):
        #解析json
        urllist=urllist['day3'];
        url_pre=config.GLOBAL_PLAYER_PRL;
        res=[];
        for url in urllist:
            obj={};
            obj['id']=(url['id']);
            obj['herf']=url_pre+(url['id']);
            obj['name']=url['soundstr'];
            res.append(obj);
        return res;
    def _get_sound_json(self,list):
        voice_json_pre=config.GLOBAL_GETSOUND_PRE;
        send_url=voice_json_pre+list['id'];
        html = urllib2.urlopen(r'%s' % send_url)
        #
        hjson = json.loads(html.read())
        mp3_url=hjson['info']['sound']['soundurl_64'];
        list['mp3_url']=config.GLOBAL_SOURCE+mp3_url;
        return list;
        # matchObj = re.search(r'/(\w*\.mp3)', mp3_name, re.M | re.I);
        # return (matchObj.group(1))
    def _get_search_voice_json(self,url):
        html = urllib2.urlopen(r'%s' % url)
        hjson = json.loads(html.read())
        if hjson['info']['pages']['item_num'] == '0':
            print('未搜索到相关音频')
            return  False;
        first_data={};
        first_data['id']= hjson['info']['model'][0]['id'];
        first_data['name']=hjson['info']['model'][0]['soundstr']
        first_data['mp3_url']=config.GLOBAL_SOURCE+hjson['info']['model'][0]['soundurl_64']
        return  first_data








