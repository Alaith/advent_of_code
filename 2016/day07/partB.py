import sys
import re

def sslpattern(frame):
	return frame[0] == frame[2] and frame[0] != frame[1]

hypernet_sep = re.compile("\[\w+\]")
hypernet_find = re.compile("\[(\w+)\]")
def ssl(s):
	supernets = hypernet_sep.split(s)
	hypernets = hypernet_find.findall(s)
	for sn in supernets:
		i = 0
		while True:
			frame = sn[i:i+3]
			if sslpattern(frame):
				for hn in hypernets:
					if (frame[1]+frame[0]+frame[1]) in hn:
						return True
			if i+3 >= len(sn):
				break
			i += 1
	return False

count = 0
for l in sys.stdin.readlines():
	if ssl(l.strip()):
		count += 1
print count
