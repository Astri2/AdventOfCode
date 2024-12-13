# 7h46 -> 7h56 end of p1
# 7h56 ->

TEST = False
import os
from collections import deque # , defaultdict
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

# areas = defaultdict(int)
# perimeters = defaultdict(int)
map = lines
visited = [[False for _ in range(len(map[0]))] for _ in range(len(map))]

def run(i, j, plot_type):
    s = deque()
    s.append((i,j))
    area = 0
    perimeter = 0
    while s:
        i_, j_ = s.pop()

        if i_ < 0 or j_ < 0 or i_ >= len(map) or j_ >= len(map[0]) or map[i_][j_] != plot_type:
            perimeter+=1
            continue

        if visited[i_][j_]: 
            continue

        area+=1
        visited[i_][j_] = True
        s.append((i_+1,j_))
        s.append((i_,j_+1))
        s.append((i_-1,j_))
        s.append((i_,j_-1))
    return area, perimeter

res = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if not visited[i][j]:
            a, p = run(i, j , map[i][j])
            res += a*p
            # areas[map[i][j]] += a
            # perimeters[map[i][j]] += p

# print(areas)
# print(perimeters)

# res = 0
# for k in areas.keys():
#     res += areas[k]*perimeters[k]
print(res)
            
            