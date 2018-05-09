#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import urllib2
import urllib
import requests
import os
import  config

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()


    def downloadobj(self, url):
        print(url['id'])
        response = urllib2.urlopen(url['id'])
        if response.getcode() != 200:
            return None
        # print(response.read())
        return
    def download_mp3(self,mp3_data):
        print u'正在下载：%s' % mp3_data['name'];
        filePath = './voice/%s.mp3' % mp3_data['name'];
        c = "wget \"%s\" -c -T 10 -t 10 -O \"%s\"" % (mp3_data['mp3_url'], filePath)
        os.system(c.encode('utf-8'))
        return
