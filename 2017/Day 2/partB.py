import sys

t = 0
for l in sys.stdin.readlines():
	s = map(lambda x: int(x),l.split())
	f = False
	for i in range(len(s)-1):
		for j in range(i+1,len(s)):
			if s[i]%s[j] == 0:
				f = s[i] / s[j]
			if s[j]%s[i] == 0:
				f = s[j] / s[i]
			if f:
				break
		if f:
			break
	if not f:
		sys.exit(1)
	t += f
print t

