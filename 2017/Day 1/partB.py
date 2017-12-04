import sys

p = sys.stdin.read().strip()
l = len(p)
t = 0
for i in range(l):
	print str(i) + "  " + str(p[i]) + "  " + str( p[(i+(l/2))%l]) + "  " + str(i+(l/2)%l)
	if p[i] == p[(i+(l/2))%l]:
		t += int(p[i])
print t

