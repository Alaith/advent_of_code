import sys

def triangleinequality(t):
    s1, s2, s3 = t
    t1, t2, t3 = (False, False, False)
    if (s1 + s2 > s3):
        t1 = True
    if (s2 + s3 > s1):
        t2 = True
    if (s1 + s3 > s2):
        t3 = True
    return t1 and t2 and t3

count = 0
for l in sys.stdin.readlines():
    if triangleinequality(map(int,l.split())):
        count += 1

print count    
