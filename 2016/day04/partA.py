import sys
import re

r = re.compile("^(.+)-(.+?)\[(.+)\]$")

def countComp(x,y):
    ammount = cmp(x[1],y[1])
    if ammount != 0:
        return ammount
    else:
        return cmp(y[0],x[0])
        
o = 0
for l in sys.stdin:
    name, sectorID, checksum = r.match(l).groups()
    print name, sectorID, checksum
    count = {}
    for c in name:
        if c == '-':
            continue
        if c in count:
            count[c]+=1
        else:
            count[c]=1
        
    chk = sorted(count.iteritems(), cmp=countComp, reverse=True)
    valid = True
    for i in range(len(checksum)):
        if checksum[i] != chk[i][0]:
            valid = False
            break
    if valid:
        o += int(sectorID)

print o
        
