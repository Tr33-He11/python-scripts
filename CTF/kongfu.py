#!/usr/bin/env python
#-*- coding:utf-8 -*-
#西普实验吧CTF,web,天下武功唯快不破writeup
__author__ = '@S4kur4'
import urllib2
import base64
import urllib
url = "http://ctf4.shiyanbar.com/web/10.php"
req = urllib2.Request(url)
rsp = urllib2.urlopen(req)
flag = rsp.headers['FLAG']
flag = base64.b64decode(flag)
data = flag.split(':')[1]
data = urllib.urlencode({'key':data})
req = urllib2.Request(url,data)
print urllib2.urlopen(req).read()