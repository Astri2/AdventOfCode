# 9h03
# 9h26

TEST = False
import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

map = []
moves = []
i=0
while(True):
    line = lines[i]
    if line == "":
        break
    map.append([c for c in line])
    i+=1

i+=1

while i < len(lines):
    moves += [c for c in lines[i]]
    i+=1


def get_start(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "@":
                return (i,j)



pos = get_start(map)
for move in moves:
    if move == "^":
        dir = (-1,0)
    elif move == ">":
        dir = (0,1)
    elif move == "v":
        dir = (1,0)
    else:
        dir = (0,-1)

    can_move = True
    tmp_pos = pos[0]+dir[0],pos[1]+dir[1]
    while(map[tmp_pos[0]][tmp_pos[1]] in "@O"):
        tmp_pos = tmp_pos[0]+dir[0],tmp_pos[1]+dir[1]
    if map[tmp_pos[0]][tmp_pos[1]] == "#":
            # print(move)
            # [print(line) for line in map]
            continue

    while(tmp_pos != pos):
        map[tmp_pos[0]][tmp_pos[1]] = map[tmp_pos[0]-dir[0]][tmp_pos[1]-dir[1]]
        tmp_pos = tmp_pos[0]-dir[0], tmp_pos[1]-dir[1]
    map[pos[0]][pos[1]] = "."
    pos = pos[0]+dir[0],pos[1]+dir[1]

    # print(move)
    # [print(line) for line in map]

res = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] != "O":
            continue
        res += 100*i+j
print(res)

