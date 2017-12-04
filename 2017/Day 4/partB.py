import sys
import sets

t=0
for l in sys.stdin.readlines():
	ls = l.split()
	s = set(ls)
	if len(s) == len(ls):
		if len(set(map(lambda x: tuple(sorted(x)), s))) == len(s):
			t += 1
print t

