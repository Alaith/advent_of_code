import sys

north = 0
east = 0
direction = 'N'
changedir = {'N': {'L': 'W', 'R':'E'}, 'E': {'L':'N','R':'S'}, 'S': {'L':'E','R':'W'}, 'W':{'L':'S','R':'N'}}
instr = sys.stdin.read()
for instruction in instr.split(','):
    instruction = instruction.strip()
    turn = instruction[0]
    blocks = int(instruction[1:])
    direction = changedir[direction][turn]
    if direction == 'N':
        north += blocks
    elif direction == 'S':
        north -= blocks
    elif direction == 'E':
        east += blocks
    elif direction == 'W':
        east -= blocks

print abs(north)+abs(east)
