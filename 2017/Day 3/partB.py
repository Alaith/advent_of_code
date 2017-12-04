# https://oeis.org/A141481 gave me a formula
# http://pari.math.u-bordeaux.fr/gp.html gave me the answer
# Then for fun in python:
import sys
from math import sqrt, floor
import numpy as np
p = int(sys.stdin.read())
T = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
m = 6
h = m * 2 - 1
A = np.zeros((h,h), dtype=np.int)
A[m-1,m-1] = 1
for n in range(1,(h-2)**2):
	g=int(floor(sqrt(n)))
	r=(g+g%2)/2
	q=4*r**2
	d=n-q
	if n <= q-2*r:
		j = d+3*r
		k = r
	elif n <= q:
		j=r
		k=-d-r
	elif n <= q+2*r:
		j=r-d
		k=-r
	else:
		j=-r
		k=d-3*r
	j=j+m
	k=k+m
	print "{} {}".format(j,k)
	s=sum(map(lambda c: A[(c[0]+j-1,c[1]+k-1)], T))
	if s > p:
		print s
		sys.exit()
	A[j-1,k-1] = s
sys.exit(1)
