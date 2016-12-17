import hashlib
import sys

result = {}
doorid = sys.stdin.read().strip()
i = 0
while True:
    digest = hashlib.md5(doorid + str(i)).hexdigest()
    if digest[:5] == "00000":
        if digest[5] in map(str,range(0,8)) and digest[5] not in result:
            result[digest[5]] = digest[6]
    if len(result) == 8:
        break
    i += 1
print "".join(map(lambda (k,v): v, sorted(result.iteritems(), lambda x,y:cmp(x[0],y[0]))))
sys.exit()