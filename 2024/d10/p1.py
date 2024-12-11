TEST = False
import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

map = [[int(t) for t in line] for line in lines]

def run(i,j,d, res: set):
    if i < 0 or j < 0 or i > len(map)-1  or j > len(map[0])-1\
        or map[i][j] != d+1:
            return
    
    if map[i][j] == 9: 
        res.add((i,j))

    for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
        run(i+di,j+dj,d+1,res)
    
res = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j]==0:
            s = set()
            run(i,j,-1, s)
            res += len(s)

print(res)

                
