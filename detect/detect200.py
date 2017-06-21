#!/usr/bin/env python
#-*- coding:utf-8 -*-
#By http status codes to determine whether your websites are normal.
__author__ = '@S4kur4'

import urllib
import threading
import Queue
import urllib2

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"}
connectable_num = 0
unconnectable_num = 0

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
    global connectable_num
    global unconnectable_num
    while not word_queue.empty():
        attempt = word_queue.get()
        attempt_list = []
        attempt_list.append("%s" % attempt)
        for scanner in attempt_list:
            url = scanner
            try:
                r = urllib2.Request(url, headers = headers)
                response = urllib2.urlopen(r, data=None, timeout=7)
                print "\033[1;32m[+] Connectable.Status code %d => %s\033[0m" % (response.code, url)
                connectable_num += 1
            except Exception,e:
                print "\033[1;31m[-] Unconnectable. => %s\033[0m" % url
                unconnectable_num += 1

def main():
    tsk = []
    word_queue = build_weblist("./weblist.txt") #here select your weblist.txt
    for i in range(7):
        t = threading.Thread(target = scanner, args = (word_queue,))
        t.start()
        tsk.append(t)
    for t in tsk:
        t.join()
    print "\033[1;34m[*] %d sites are Connectable.\033[0m" % connectable_num
    print "\033[1;34m[*] %d sites are Unconnectable.\033[0m" % unconnectable_num

if __name__ == '__main__':
    main()