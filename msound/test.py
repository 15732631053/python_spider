



import os
song_url = 'http://static.missevan.com/MP3/201703/13/297a06ba39ab901dc538e0b0823e629c205112.mp3'
filePath = '123.mp3'
c = "wget \"%s\" -c -T 10 -t 10 -O \"%s\"" % (song_url, filePath)
os.system(c.encode('utf-8'))
