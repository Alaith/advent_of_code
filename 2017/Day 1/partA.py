import sys

p = sys.stdin.read().strip()
l = len(p)
p = p + p[0]
t = 0
for i in range(l):
	if p[i] == p[i+1]:
		t += int(p[i])
print t

