import sys

def pattern(frame):
	return frame[0] == frame[3] and frame[1] == frame[2] and frame[0] != frame[1]

def match(s):
	abba = False
	ainh = False
	hypernet = False
	i = 0
	while True:
		frame = s[i:i+4]
		if frame[3] == '[' or frame[3] == ']':
			hypernet = not hypernet
			i += 4
			continue
		if pattern(frame):
			if hypernet:
				ainh = True
				break
			else:
				abba = True
		if i + 4 >= len(s):
			break
		i += 1
	if abba and not ainh:
		return True
	return False

count = 0
for l in sys.stdin.readlines():
	if match(l.strip()):
		count += 1
print count
