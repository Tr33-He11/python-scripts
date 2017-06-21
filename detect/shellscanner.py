#!/usr/bin/env python
#-*- coding:utf-8 -*-
#This script help you find webshells in your Server use RE
__author__ = 'S4kur4'
name = "      _          _ _                                     \n"\
       "     | |        | | |                                    \n"\
       "  ___| |__   ___| | |___  ___ __ _ _ __  _ __   ___ _ __ \n"\
       " / __| '_ \ / _ \ | / __|/ __/ _` | '_ \| '_ \ / _ \ '__|\n"\
       " \__ \ | | |  __/ | \__ \ (_| (_| | | | | | | |  __/ |   \n"\
       " |___/_| |_|\___|_|_|___/\___\__,_|_| |_|_| |_|\___|_|   \n"\
       "                                                           "

import os
import re
import optparse
import time
import sys

regex1 = r'((?:eval|eval_r|execute|ExecuteGlobal)\s*?\(?request)' #asp
regex2 = r'((?:exec|base64_decode|edoced_46esab|eval|eval_r|system|proc_open|popen|curl_exec|curl_multi_exec|parse_ini_file|show_source|assert)\s*?\(\$(?:_POST|_GET|_REQUEST|GLOBALS))' #php
regex3 = r'((?:_POST|_GET|_REQUEST|GLOBALS)\[(?:.*?)\]\(\$(?:_POST|_GET|_REQUEST|GLOBALS))' #php
regex4 = r'write\(request\.getParameter' #jsp
regex5 = r'((?:eval|eval_r|execute|ExecuteGlobal).*?request)' #aspx
regex6 = r'SaveAs\(\s*?Server\.MapPath\(\s*?Request' #aspx
regex7 = r'(pw|pwd|pass|passwd|password|passwords)' #passwords

def filematch(filepath):
	if os.path.isfile(filepath):
		hellofile = open(filepath)
		filetext = hellofile.read()
		mo1 = re.compile(regex1, re.I).search(filetext)
		mo2 = re.compile(regex1, re.I).search(filetext)
		mo3 = re.compile(regex1, re.I).search(filetext)
		mo4 = re.compile(regex1, re.I).search(filetext)
		mo5 = re.compile(regex1, re.I).search(filetext)
		mo6 = re.compile(regex1, re.I).search(filetext)
		mo7 = re.compile(regex1, re.I).search(filetext)
		mo8 = re.compile(regex7, re.I).search(filetext)
		if (mo1 or mo2 or mo3 or mo4 or mo5 or mo6 or mo7 or mo8) == None:
			print "\033[1;32m[normal]:" + filepath + " [createTime]:" + time.ctime(os.path.getctime(filepath))+"\033[0m"
		else:
			print "\033[1;31m[suspect]:" + filepath + " [createTime]:" + time.ctime(os.path.getctime(filepath))+"\033[0m"
		hellofile.close()
	else:
		print "File does not exist!"

def filescan(floderpath):
	for parent, dirnames, filenames in os.walk(floderpath):
		for filename in filenames:
			filepath = os.path.join(parent,filename)
			filematch(filepath)
	
def main():
	print name
	print "[Author]:%s\n[Site]:http://rid.red\n[Mail]:s4kur4s4kur4@gmail.com" % __author__
	parser = optparse.OptionParser('usage: %prog [options]')
	parser.add_option('-p', '--path', dest='path', type='string', help='specify a folder path you want to scanner')
	(options, args) = parser.parse_args()
	if (options.path == None):
		parser.print_help()
		sys.exit(0)
	else:
		floderpath = options.path
		filescan(floderpath)

if __name__ == '__main__':
	main()