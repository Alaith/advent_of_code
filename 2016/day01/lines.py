import sys
from shapely.geometry import LineString

north = 0
east = 0
direction = 'N'
changedir = {'N': {'L': 'W', 'R':'E'}, 'E': {'L':'N','R':'S'}, 'S': {'L':'E','R':'W'}, 'W':{'L':'S','R':'N'}}
segments = []

def intersection(s0, s1):
    i = LineString(s0).intersection(LineString(s1))
    if i:
        return (i.x, i.y)
    return None

instr = sys.stdin.read()
for instruction in instr.split(','):
    instruction = instruction.strip()
    turn = instruction[0]
    blocks = int(instruction[1:])
    direction = changedir[direction][turn]
    startlocation = (east, north)
    if direction == 'N':
        north += blocks
    elif direction == 'S':
        north -= blocks
    elif direction == 'E':
        east += blocks
    elif direction == 'W':
        east -= blocks
    endlocation = (east,north)
    sn = (startlocation, endlocation)
    for s in segments[:-1]:
        i = intersection(s, sn)
        if i:
            print abs(i[0])+abs(i[1])
            sys.exit(0)
    segments.append(sn)

print abs(north)+abs(east)
sys.exit(1)
