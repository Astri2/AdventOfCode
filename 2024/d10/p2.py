TEST = False
import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

map = [[int(t) for t in line] for line in lines]

def run(i,j,d):
    if i < 0 or j < 0 or i > len(map)-1  or j > len(map[0])-1 or map[i][j] != d+1:
            return 0
    
    if map[i][j] == 9: 
        return 1

    r = 0
    for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
        r+=run(i+di,j+dj,d+1)
    return r
    
res = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j]==0:
            res+=run(i,j,-1)

print(res)

                
