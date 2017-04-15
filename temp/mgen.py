#!/usr/bin/python
__author__ = "sungpi"

import os
import sys, getopt 

def main(argv):
	time = 0
	try:
		opts, args = getopt.getopt(argv, "t:")
	except getopt.GetoptError:
		print "mgen.py -t <expires_after_t_seconds>"
	for opt, arg in opts:
		if opt == '-t':
			time = arg
	print "will expire after ", time, "seconds"
	
#	os.system('./a')
	

if __name__ == "__main__":
	main(sys.argv[1:])
	
