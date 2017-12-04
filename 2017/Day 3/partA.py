import sys
from math import floor, sqrt
p = int(sys.stdin.read())


#A214526 
#https://math.stackexchange.com/questions/163080/on-a-two-dimensional-grid-is-there-a-formula-i-can-use-to-spiral-coordinates-in

def coords(n):
	# n steps
	m = floor(sqrt(n))
	k = (m-1)/2 if m%2 !=0 else m/2 if n >= m*(m+1) else m/2-1
	if 2*k*(2*k+1) < n and n <= (2*k+1)**2:
		return (n-4*k**2-3*k, k)
	if (2*k+1)**2 < n and n <= 2*(k+1)*(2*k+1):
		return (k+1, 4*k**2+5*k+1-n)
	if 2*(k+1)*(2*k+1) < n and n <= 4*(k+1)**2:
		return (4*k**2+7*k+3-n, -k-1)
	if 4*(k+1)**2 < n and n <= 2*(k+1)*(2*k+3):
		return (-k-1, n-4*k**2-9*k-5)
	raise Exception()

def dist(a,b):
	return abs(a[0]-b[0]) + abs(a[1]-b[1])

print dist((0,0),coords(p-1))

