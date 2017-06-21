#!/usr/bin/env python
#-*- coding:utf-8 -*-
#This is a tool to decrypt caesar password, it can list all possible cases.
__author__ = '@S4kur4'
import optparse
import sys

payload = 'abcdefghijklmnopqrstuvwxyz'

def main():
	parser = optparse.OptionParser('usage: %prog [options]')
	parser.add_option('-p', '--password', dest='password', type='string', help='specify a caesar password to decrypt')
	(options, args) = parser.parse_args()
	if (options.password == None):
		parser.print_help()
		sys.exit(0)
	else:
		password = options.password
	for i in range(26):
		str1 = ''
		for word in password:
			if 96 < ord(word) < 123:
				str1 = str1 + payload[((ord(word)+i)-97)%26]
			else:
				str1 = str1 + word
		print "[offset %d]: %s" %(i, str1)

if __name__ == '__main__':
	main()