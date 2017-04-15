#!/usr/bin/python

import subprocess
subprocess.call('a')
cmd = ['a', '-t', '100']
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
for line in p.stdout:
	print line
p.wait()
print p.returncode
