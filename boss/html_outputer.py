#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
class HtmlOutputer(object):

    def __init__(self):
        self.datas = []


    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self,page):
        htmlpage='%s' % page;
        fout = open(htmlpage+'.html', 'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td ><a href=%s>链接</a></td>" % data['url'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()