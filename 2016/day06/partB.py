import sys
import collections

result = ''
counts = []
for l in sys.stdin.readlines():
	i = 0
	for c in l.strip():
		if i >= len(counts):
			counts.append(collections.Counter())
		counts[i].update(c)
		i += 1
for c in counts:
	result += sorted(dict(c).iteritems(),lambda x,y:cmp(x[1],y[1]))[0][0]
print result
