# stop : 7h05
# restart : 10h21 - 10h44
# restart : 11h00 - 11h25
# restart 
TEST = False
import os
from collections import defaultdict
from copy import deepcopy
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test2" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

map = [[""]*len(lines[0]) for _ in range(len(lines))]
next_dirs = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
dir_to_int = {'^': 0, '>': 1, 'v': 2, '<': 3}
dirs = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}

def run(pos: tuple[int, int, str]) -> set[tuple[int, int]]:
    visited_pos = set()
    visited_pos.add(pos)
    while True:

        dir = pos[2]
        i_, j_ = pos[0]+dirs[dir][0], pos[1]+dirs[dir][1]

        # exits the map
        if i_ < 0 or i_ == len(lines) or j_ < 0 or j_ == len(lines[0]):
            break
        elif map[i_][j_] == '#':
            # turn right
            pos = (pos[0], pos[1], next_dirs[dir])
            if pos in visited_pos: return -1
        else: 
            pos = i_, j_, dir
            if pos in visited_pos: return -1
            visited_pos.add(pos)

    # extract only location, ignore direction
    uniq_pos = {(p[0], p[1]) for p in visited_pos}
    return uniq_pos

def main():
    for i,line in enumerate(lines):
        for j,c in enumerate(line):
            if c in '^>v<':
                map[i][j] = '.'
                start = (i, j, c)
            else: map[i][j] = c
    uniq_pos = run(start)
    assert uniq_pos != -1
    print("P1", len(uniq_pos))

    # in p2 we can't place on spawn point
    if (start[0], start[1]) in uniq_pos: uniq_pos.remove((start[0], start[1]))

    legit_blocks = 0
    for i, pos in enumerate(uniq_pos):
        i,j = pos
        map[i][j] = "#"
        if(run(start) == -1): legit_blocks+=1
        map[i][j] = "."
    print("P2", legit_blocks)

if __name__ == "__main__":
    main()
