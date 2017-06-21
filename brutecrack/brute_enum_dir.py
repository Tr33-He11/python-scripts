#!/usr/bin/env python
#-*- coding:utf-8 -*-
#This program can help you brute enumerate target sites may existing directory or manage pages.
#You should specify your own path or directory dictionary files.
__author__ = "@S4kur4"

import urllib
import urllib2
import threading
import Queue
import optparse
import sys

resume = None
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0"

def build_wordlist(pathlist_file):
    fd = open(pathlist_file, "rb")
    raw_words = fd.readlines()
    fd.close()
    found_resume = False
    words = Queue.Queue()
    for word in raw_words:
        word = word.rstrip()
        if resume is not None:
            if found_resume:
                words.put(word)
            else:
                if word == resume:
                    found_resume = True
                    print "Resuming wordlist from: %s" % resume
        else:
            words.put(word)
    return words

def dir_bruter(word_queue, target_url):
    while not word_queue.empty():
        attempt = word_queue.get()
        attempt_list = []
        if "." not in attempt:
            attempt_list.append("%s/" % attempt)
        else:
            attempt_list.append("%s" % attempt)
        for brute in attempt_list:
            url = "%s%s" % (target_url, urllib.quote(brute))
            try:
                headers = {}
                headers["User-Agent"] = user_agent
                r = urllib2.Request(url, headers = headers)
                response = urllib2.urlopen(r)
                if len(response.read()):
                    print "[%d]%s" % (response.code, url)
            except urllib2.URLError,e:
                pass

def main():
	parser = optparse.OptionParser('usage: %prog [options]')
	parser.add_option('-u', '--url', dest='target_url', type='string', help='specify target URL')
	parser.add_option('-d', '--dict', dest='pathlist_file', type='string', help='specify path dictionary file')
	parser.add_option('-t', '--threads', dest='threads', default=20, type='int', help='specify threads number')
	(options, args) = parser.parse_args()
	if (options.target_url == None) | (options.pathlist_file == None):
		parser.print_help()
		sys.exit(0)
	else:
		target_url = options.target_url
		pathlist_file = options.pathlist_file
		threads = options.threads
	target_url = target_url.rstrip('/')
	word_queue = build_wordlist(pathlist_file)
	for i in range(threads):
		t = threading.Thread(target = dir_bruter, args = (word_queue, target_url))
		t.start()

if __name__ == '__main__':
	main()