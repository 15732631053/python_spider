# encoding: utf-8
import os
import urllib2
import json
url_header='http://www.missevan.com/sound/getsound?soundid=';
static_header='http://static.missevan.com/';
for num in range(21000,22002):
    json_url=url_header+str(num);
    html = urllib2.urlopen(r'%s' % json_url);
    hjson = json.loads(html.read())
    if hjson['state']!='error':
        mp3_url=static_header+hjson['info']['sound']['soundurl_64'];
        mp3_name=hjson['info']['sound']['soundstr'];
        # print mp3_url;
        filePath = './voice/%s.mp3' % mp3_name;
        c = "wget \"%s\" -c -T 10 -t 10 -O \"%s\"" % (mp3_url, filePath)
        os.system(c.encode('utf-8'))
    else:
        print 'error';


#  filePath = './voice/%s.mp3' % mp3_data['name'];
#  c = "wget \"%s\" -c -T 10 -t 10 -O \"%s\"" % (mp3_data['mp3_url'], filePath)
# os.system(c.encode('utf-8'))
