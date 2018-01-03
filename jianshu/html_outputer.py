#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
class HtmlOutputer(object):

    def __init__(self):
        self.datas = []



    def collect_data(self, data):
        if data is None:
            return
        self.datas=data



    def output_html(self,num):
        num=num-1;
        if num==0:
            return ;
        new_str = '%d' % num
        fout = open('./html/'+new_str+'.html', 'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<h1 ><a href=%s>链接</a></h1>" % self.datas['url'].encode('utf-8'))
        fout.write("<h2>%s</h2>" % self.datas['title'].encode('utf-8'))
        fout.write("<h3>%s</h3>" % self.datas['summary'].encode('utf-8'))
        fout.write("</body>")
        fout.write("</html>")
        fout.close()