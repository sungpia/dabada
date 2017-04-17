#!/usr/bin/python
__author__ = "sungpi"

import os
import sys, getopt 
import subprocess
import threading

class run_cmd(threading.Thread):
	def __init__(self, cmd, timeout):
		threading.Thread.__init__(self)
		print cmd 
		print timeout
		self.cmd = cmd
		self.timeout = int(timeout)
	
	def run(self):
		self.p = subprocess.Popen(self.cmd)
		self.p.wait()

	def Run(self):
		self.start()
		self.join(self.timeout)
		
		if self.is_alive():
			self.p.terminate()
			self.join()

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
	
	run_cmd(["mgen ipv4 interface enp4s0 input script.mgn hostAddr on"], time).Run()
		

if __name__ == "__main__":
	main(sys.argv[1:])
	
