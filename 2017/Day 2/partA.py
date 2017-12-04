import sys

t = 0
for l in sys.stdin.readlines():
	s = l.split()
	rmin = int(s[0])
	rmax = int(s[0])
	for v in s:
		iv = int(v)
		if rmin > iv:
			rmin = iv
		if rmax < iv:
			rmax = iv
	t += rmax - rmin
print t

