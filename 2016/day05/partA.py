import hashlib
import sys

result = ""
doorid = sys.stdin.read().strip()
i = 0
while True:
    digest = hashlib.md5(doorid + str(i)).hexdigest()
    if digest[:5] == "00000":
        result += digest[5]
    if len(result) == 8:
        break
    i += 1
print result
sys.exit()