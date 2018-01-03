#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import urllib2
import random
import proxyip;
class HtmlDownloader(object):



    def download(self, url):
        # proxies = proxyip.getListProxies()
        if url is None:
            return None
        # random_proxy = random.choice(proxies)
        # proxy_support = urllib2.ProxyHandler({"http":'113.121.241.36'})
        # opener = urllib2.build_opener(proxy_support)
        # urllib2.install_opener(opener)
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()