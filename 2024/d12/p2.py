# 7h46 -> 7h56 end of p1
# 7h56 -> 8h00l
TEST = False
import os
from collections import deque # , defaultdict
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

map = [[c for c in line]for line in lines]
visited = [[False for _ in range(len(map[0]))] for _ in range(len(map))]

def run(i0, j0, plot_type, id):
    min_i, min_j, max_i, max_j = 99999,99999,0,0
    s = deque()
    s.append((i0,j0))
    area = 0
    perimeter = 0
    while s:
        i, j = s.pop()

        if i < 0 or j < 0 or i >= len(map) or j >= len(map[0]) or map[i][j] != plot_type:
            perimeter+=1
            continue

        if visited[i][j]: 
            continue

        area+=1
        min_i = min(min_i, i); min_j = min(min_j, j)
        max_i = max(max_i, i); max_j = max(max_j, j)
        map[i][j] = id
        visited[i][j] = True
        s.append((i+1,j))
        s.append((i,j+1))
        s.append((i-1,j))
        s.append((i,j-1))

    sides = 0
    for i in range(min_i, max_i+1):
        side_top = False
        side_bot = False
        for j in range(min_j, max_j+1):
            
            # concave
            if map[i][j] != id:
                side_top = False
                side_bot = False
                continue

            # convexe
            if side_top and i != 0 and map[i-1][j] == id:
                side_top = False
            if side_bot and i != len(map)-1 and map[i+1][j] == id:
                side_bot = False

            # new top border
            if not side_top and (i == 0 or map[i-1][j] != id):
            # if not side_top and i != 0 and map[i-1][j] != id:
                side_top = True
                sides +=1

            # new bottom border
            if not side_bot and (i == len(map)-1 or map[i+1][j] != id):
            # if not side_bot and i != len(map)-1 and map[i+1][j] != id:
                side_bot = True
                sides +=1
            
    for j in range(min_j, max_j+1):
        side_left = False
        side_right = False
        for i in range(min_i, max_i+1):
            # concave
            if map[i][j] != id:
                side_left = False
                side_right = False
                continue

            # convexe
            if side_left and j != 0 and map[i][j-1] == id:
                side_left = False
            if side_right and j != len(map[0])-1 and map[i][j+1] == id:
                side_right = False

            # new left border
            if not side_left and (j == 0 or map[i][j-1] != id):
                side_left = True
                sides +=1

            # new right border
            if not side_right and (j == len(map[0])-1 or map[i][j+1] != id):
                side_right = True
                sides +=1
    
    return area, perimeter, sides


res = 0
res2 = 0
id = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if not visited[i][j]:
            # print(map[i][j])
            area, peri, nb_sides = run(i, j , map[i][j], id)
            # print(area, peri, nb_sides)
            id+=1
            res += area*peri
            res2 += area*nb_sides
print("p1", res)            
print("p2", res2)