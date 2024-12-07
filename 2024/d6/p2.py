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
dirs = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}

next_dirs = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
def turn(pos):
    return pos[0], pos[1], next_dirs[pos[2]]

def move(pos):
    return pos[0]+dirs[pos[2]][0], pos[1]+dirs[pos[2]][1], pos[2]

def move_back(pos):
    return pos[0]-dirs[pos[2]][0], pos[1]-dirs[pos[2]][1], pos[2]

def run(pos: tuple[int, int, str]) -> set[tuple[int, int]]:
    visited_pos = set()
    visited_pos.add(pos)
    while True:

        i_, j_, dir = move(pos)

        # exits the map
        if i_ < 0 or i_ == len(lines) or j_ < 0 or j_ == len(lines[0]):
            break
        elif map[i_][j_] == '#':
            # turn right
            pos = turn(pos)
            if pos in visited_pos: return -1
        else: 
            pos = i_, j_, dir
            if pos in visited_pos: return -1
            visited_pos.add(pos)

    return visited_pos

def main():
    for i,line in enumerate(lines):
        for j,c in enumerate(line):
            if c in '^>v<':
                map[i][j] = '.'
                start = (i, j, c)
            else: map[i][j] = c

    uniq_pos_dir = run(start)
    assert uniq_pos_dir != -1

    # extract only location, ignore direction
    uniq_pos = {(p[0], p[1]) for p in uniq_pos_dir}
    print("P1", len(uniq_pos))

    # in p2 we can't place on spawn point
    if (start[0], start[1]) in uniq_pos: uniq_pos.remove((start[0], start[1]))

    legit_block_pos = set()
    for i, pos in enumerate(uniq_pos):
        i,j = pos
        map[i][j] = "#"
        if(run(start) == -1): 
            legit_block_pos.add((i,j))
        map[i][j] = "."
    if (start[0], start[1]) in legit_block_pos: legit_block_pos.remove((start[0], start[1]))
    print("P2", len(legit_block_pos))

if __name__ == "__main__":
    main()
