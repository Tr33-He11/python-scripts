#!/usr/bin/env python
#-*- coding:utf-8 -*-
#By http status codes to determine whether your websites are normal.
__author__ = '@S4kur4'

import urllib
import threading
import Queue
import urllib2

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"

def build_weblist(weblist_file):
    fd = open(weblist_file, "rb")
    raw_words = fd.readlines()
    fd.close()
    words = Queue.Queue() 
    for word in raw_words:
        word = word.rstrip()
        words.put(word)
    return words

def scanner(word_queue):
    while not word_queue.empty(): 
        attempt = word_queue.get()
        attempt_list = []
        attempt_list.append("%s" % attempt)
        for scanner in attempt_list:
            url = scanner
            try:
                headers = {}
                headers["User-Agent"] = user_agent
                r = urllib2.Request(url, headers = headers)
                response = urllib2.urlopen(r, data=None, timeout=10)
                print "[+]%d => %s" % (response.code, url)
            except Exception,e:
                print "[Unconnected] => %s" % url

def main():
	word_queue = build_weblist("/../weblist.txt") #here select your weblist.txt
	for i in range(30):
		t = threading.Thread(target = scanner, args = (word_queue, ))
		t.start()

if __name__ == '__main__':
	main()