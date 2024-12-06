# start 6h03
TEST = False
import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

map = [[""]*len(lines[0]) for _ in range(len(lines))]

next_dirs = {"^": ">", ">": "v", "v": "<", "<": "^"}
dirs = {"^": (-1,0), ">": (0,1), "v": (1,0), "<": (0,-1)}
start = (-1, -1, -1)
for i,line in enumerate(lines):
    for j,c in enumerate(line):
        if c in '^>v<':
            map[i][j] = "X"
            start = (i,j, c)
        else: map[i][j] = c
pos = start
step = 0
while True:
    dir = pos[2]
    i_, j_ = pos[0]+dirs[dir][0], pos[1]+dirs[dir][1]

    if i_ < 0 or i_ == len(lines) or j_ < 0 or j_ == len(lines[0]):
        [print("".join(line)) for line in map]
        print("res",sum([line.count('X') for line in map]))
        print("steps",step)
        exit(0)

    if map[i_][j_] == "#":
        pos = pos[0], pos[1], next_dirs[dir]        
    else: 
        step+=1
        pos = i_, j_, dir
        map[pos[0]][pos[1]] ='X'
