from collections import deque

with open("d7/input.txt") as f:
    lines = f.read().splitlines()

map = []

for i, line in enumerate(lines):
    map.append(list(line))
    idx = line.find("S")
    if(idx != -1):
        start = (i, idx)

print(start)

to_expand = deque()
splits = set()

to_expand.append(start)
while(to_expand):
    i,j = to_expand.popleft()
    
    # reached the bottom
    if(i == len(lines)-1): continue 
    
    if(map[i+1][j] == "^"):
        # already split, nothing to do
        if((i+1, j) not in splits): splits.add((i+1, j))

        if(map[i+1][j+1] == "."):
            map[i+1][j+1] = "|"
            to_expand.append((i+1, j+1))
        if(map[i+1][j-1] == "."):
            map[i+1][j-1] = "|"
            to_expand.append((i+1, j-1))
    elif(map[i+1][j] == "."):
        map[i+1][j] = "|"
        to_expand.append((i+1, j))

print()
# [print("".join(l)) for l in map]
print(len(splits))
