#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import urllib2
import urllib
import time

class HtmlDownloader(object):
    def __init__(self):
        self.img = set();
    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
    def collect_img(self, data):
        if data is None:
            return
        self.img=self.img.union(data)
    def downloadImg(self,imglist):
        x = 1
        for img in imglist:
            urllib.urlretrieve(img,'./image/%s.jpg' % x)
            x+=1;