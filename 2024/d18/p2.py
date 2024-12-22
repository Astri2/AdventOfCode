TEST = False
import os
from collections import deque
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

stop = 12 if TEST else 1024
map_size = 7 if TEST else 71
map = [['.' for _ in range(map_size)] for _ in range(map_size)]


lines = [tuple(int(n) for n in line.split(",")) for line in lines]



for i,j in lines[:stop]:
    map[j][i] = '#'
    
[print("".join(line)) for line in map]

to_add = stop
while True:

    i_add,j_add = lines[to_add]
    to_add+=1
    map[j_add][i_add] = '#'
    
    dist = 0
    visited = set()
    to_visit = deque()
    to_visit.append((map_size-1,map_size-1))

    while (0,0) not in visited and to_visit:
        dist+=1
        next_to_visit = deque()
        for i,j in to_visit:
            if (i,j) in visited or i < 0 or i >= map_size or j < 0 or j >= map_size:
                continue
            
            visited.add((i,j))
            
            if map[i][j] == '#':
                continue
            
            next_to_visit.append((i+1,j))
            next_to_visit.append((i-1,j))
            next_to_visit.append((i,j+1))
            next_to_visit.append((i,j-1))
            
        to_visit = next_to_visit
    
    if (0,0) not in visited:
        print(i_add,j_add,sep=",")
        exit(0)
    # print(dist-1, (0,0) in visited)