import sys
import sets

t=0
for l in sys.stdin.readlines():
	s = l.split()
	if len(set(s)) == len(s):
		t += 1	
print t

