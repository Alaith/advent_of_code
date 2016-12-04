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
while(True):
    t = zip(*[map(int,sys.stdin.readline().split()),map(int,sys.stdin.readline().split()),map(int,sys.stdin.readline().split())])
    if len(t) == 0: 
        break
    for i in t:
        if triangleinequality(i):
            count += 1

print count    
