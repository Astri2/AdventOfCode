# 14h19 14h34
# 15j20 15h31 (p1)
from collections import defaultdict
TEST = False
import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

map = [['#' if c == '#' else 10000 for c in line] for line in lines]

def find_start_end():
    i_s,j_s = -1,-1
    i_e,j_e = -1,-1
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "S":
                i_s, j_s = i,j
            if lines[i][j] == "E":
                i_e,j_e = i,j
    return i_s, j_s, i_e, j_e

i_s, j_s, i_e, j_e = find_start_end()

# path setup
to_visit = [(i_s, j_s)]
visited = set()
dist = 0
while to_visit:
    to_visit_next = []
    for i,j in to_visit:
        if (i,j) in visited or i < 0 or j < 0 or i >= len(map) or j >= len(map[0]):
            continue
        visited.add((i,j))
        if map[i][j] == "#": continue
        
        if map[i][j] <= dist: continue
        
        map[i][j] = dist
        
        # no exit from end
        if (i,j) == (i_e,j_e): continue
        
        to_visit_next.append((i-1,j))
        to_visit_next.append((i+1,j))
        to_visit_next.append((i,j-1))
        to_visit_next.append((i,j+1))
    to_visit = to_visit_next
    
    dist+=1
    
def disp():
    for line in map:
        for c in line:
            print("    #" if c == "#" else f"{c:-5}", end= "")
        print()
    

shortcuts = defaultdict(int)
dist_cap = 20
for i in range(len(map)):
    for j in range(len(map[0])):
        c = map[i][j]
        # wall or unset
        if c == "#" or c == 10000: continue
        
        for i_ in range(max(0,i-dist_cap), min(len(map), i+dist_cap+1)):
            for j_ in range(max(0, j-dist_cap), min(len(map[0]), j+dist_cap+1)):
                
                # distance L1
                if abs(i-i_)+abs(j-j_) > dist_cap: continue
                
                c2 = map[i_][j_]
                if c2 == "#" or c2 == 10000 or c >= c2: continue
                
                shortcuts[c2-c-abs(i_-i)-abs(j_-j)]+=1
        
        # if i >= 2:
        #     c2 = map[i-2][j]
        #     if c2 != "#" and c2 != 10000 and c < c2:
        #         shortcuts[abs(c2-c)-2]+=1
        # if j >= 2:
        #     c2 = map[i][j-2]
        #     if c2 != "#" and c2 != 10000 and c < c2:
        #         shortcuts[abs(c2-c)-2]+=1
                
        # if i < len(map)-2:
        #     c2 = map[i+2][j]
        #     if c2 != "#" and c2 != 10000 and c < c2:
        #         shortcuts[abs(c2-c)-2]+=1
                
        # if j < len(map[0])-2:
        #     c2 = map[i][j+2]
        #     if c2 != "#" and c2 != 10000 and c < c2:
        #         shortcuts[abs(c2-c)-2]+=1

# div by 2 bc it's 2 ways
cap = 64 if TEST else 100
res = 0
for k,v in shortcuts.items():
    if k >= cap:
        res+=v
print(res)
                