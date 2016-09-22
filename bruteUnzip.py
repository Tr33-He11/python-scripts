#!/usr/bin/env python
#-*- coding:utf-8 -*-
#This is a tool to brute unzip ZIP file, use your own password dictionary file.
__author__ = '@S4kur4'

import zipfile
import optparse
import threading
import sys

fell = 0

def extractFile(zFile, password):
	global fell
	try:
		zFile.extractall(pwd = password)
		print '[+]Password found: %s' % password
		fell = 1
	except:
		pass

def main():
	parser = optparse.OptionParser('usage: %prog [Options]')
	parser.add_option('-f', '--file', dest='zip_file', type='string', help='specify a zip file')
	parser.add_option('-d', '--dict', dest='pass_dict', type='string', help='specify password dictionary file')
	parser.add_option('-t', '--threads', dest='threads', default=20, type='int', help='specify threads number')
	(options, args) = parser.parse_args()
	if (options.zip_file == None) | (options.pass_dict == None):
		parser.print_help()
		sys.exit(0)
	else:
		zip_file = options.zip_file
		pass_dict = options.pass_dict
	zFile = zipfile.ZipFile(zip_file)
	passFile = open(pass_dict)
	for line in passFile.readlines():
		password = line.strip('\n')
		t = threading.Thread(target=extractFile, args=(zFile, password))
		t.start()
	if fell == 0:
		print "[-]Password not found"

if __name__ == '__main__':
	main()