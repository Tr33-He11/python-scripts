#!/usr/bin/env python
#-*- coding:utf-8 -*-
#ceye.io
__author__ = '@S4kur4'
logo = "\033[1;34m"\
       "  ________  __  _____    (_)___  \n"\
       " / ___/ _ \/ / / / _ \  / / __ \ \n"\
       "/ /__/  __/ /_/ /  __/ / / /_/ / \n"\
       "\___/\___/\__, /\___(_)_/\____/  \n"\
       "         /____/                  \n"\
       "   Discover SSRF/RCE/XXE/RFI\033[0m"

import requests
import sys
import json
import optparse

apitoken = "xxxxxxxxxxxxxxxxxxxxxxx" #here set your api token
header1 = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Accept" : "*/*"
    }

def main():
    print logo
    parser = optparse.OptionParser('Usage: %prog [options]\nExample: %prog -t dns -f bbs')
    parser.add_option('-t', '--type', dest='querytype', type='string', help='specify query type, \'dns\' or \'request\'')
    parser.add_option('-f', '--filter', dest='queryfilter', type='string', help='specify query filter, a keyword', default='')
    (options, args) = parser.parse_args()
    if options.querytype == None:
        parser.print_help()
        sys.exit(0)
    else:
         querytype = options.querytype
         queryfilter = options.queryfilter
    queryurl = "http://ceye.io/api/record?token={0}&type={1}&filter={2}".format(apitoken, querytype, queryfilter)
    try:
    	print "\033[1;32mQuerying, please wait for a while...\033[0m"
    	response = requests.get(url=queryurl)
    	result_json = json.loads(response.text)
    	if querytype == 'dns':
    		for i in range(0, len(result_json)+1):
    			print "\033[1;32m[+]\033[0m \033[1;33mTIME:\033[0m%s \033[1;33mIP:\033[0m%s \033[1;33mNAME:\033[0m%s" % (result_json[i]['time'], result_json[i]['remote_addr'], result_json[i]['name'])
    	if querytype == 'request':
    		for i in range(0, len(result_json)+1):
    			print "\033[1;32m[+]\033[0m \033[1;33mTIME:\033[0m%s \033[1;33mIP:\033[0m%s \033[1;33mURL:\033[0m%s" % (result_json[i]['time'], result_json[i]['remote_addr'], result_json[i]['url'])
    except Exception, e:
    	pass

if __name__ == '__main__':
    main()