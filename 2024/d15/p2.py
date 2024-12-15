# 9h03 # 9h26 P1
# 13h56 -> 2h42

TEST = False
import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

replaces = {".": "..", "#": "##", "O": "[]", "@": "@."}

map = []
moves = []
i=0
while(True):
    line = lines[i]
    if line == "":
        break
    map.append([])
    for c in line:
        chars = replaces[c]
        map[-1].append(chars[0])
        map[-1].append(chars[1])
    # map.append([c for c in line])
    i+=1

i+=1

while i < len(lines):
    moves += [c for c in lines[i]]
    i+=1

def get_start(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "@":
                return (i,j, '@')


# def do_the_move(pos: tuple[int, int], dir: tuple[int, int], moving: set[tuple[int, int]]) -> tuple[int, int]:
#     t = map[pos[0]][pos[1]]
#     p2 = pos[0]+dir[0], pos[1]+dir[1]
#     t2 = map[p2[0]][p2[1]]
#     if(t2 == "#"): return False
    
#     can_move = True
#     if(t2 == "[" and not p2 in moving):
#         moving.add(p2)
#         moving.add((p2[0],p2[1]+1))
#         can_move &= do_the_move((p2[0],p2[1]+1),dir,moving)
#         can_move &= do_the_move(p2,dir, moving)
#     elif(t2 == "]" and not p2 in moving):
#         moving.add(p2)
#         moving.add((p2[0],p2[1]-1))
#         can_move &= do_the_move((p2[0],p2[1]-1),dir, moving)
#         can_move &= do_the_move(p2,dir, moving)
    
#     if can_move:
#         map[p2[0]][p2[1]] = t
#         map[pos[0]][pos[1]] = "."
        
#         return True
    
#     return False

def can_move(pos: tuple[int, int], dir: tuple[int, int]) -> list[set[tuple[int, int, str]]]:
    to_move: list[set[tuple[int, int, str]]] = [{pos}]
    while(len(to_move[-1]) != 0):
        to_move.append(set())
        for p in to_move[-2]:
            p2 = p[0]+dir[0],p[1]+dir[1], map[p[0]+dir[0]][p[1]+dir[1]]
            
            if p2[2] == "#":
                return False
            if p2[2] == "[" and not p2 in to_move[-2]:
                to_move[-1].add((p2[0],p2[1]+1,']'))
                to_move[-1].add(p2)
            if p2[2] == "]" and not p2 in to_move[-2]:
                to_move[-1].add((p2[0],p2[1]-1,'['))
                to_move[-1].add(p2)
    return to_move

# [print("".join(l)) for l in map]
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
    
    to_move = can_move(pos, dir)
    
    if(to_move == False): continue
    
    # clear all old tiles
    for move_gen in to_move:
        for p in move_gen:
            map[p[0]][p[1]] = "."
    
    # right new pos
    for move_gen in to_move[::-1]:
        for p in move_gen:
            map[p[0]+dir[0]][p[1]+dir[1]] = p[2]

    pos = pos[0]+dir[0],pos[1]+dir[1],'@'
    
    # [print("".join(line)) for line in map]
    
    # can_move = True
    # tmp_pos = pos[0]+dir[0],pos[1]+dir[1]
    # while(map[tmp_pos[0]][tmp_pos[1]] in "@O"):
    #     tmp_pos = tmp_pos[0]+dir[0],tmp_pos[1]+dir[1]
    # if map[tmp_pos[0]][tmp_pos[1]] == "#":
    #         # print(move)
    #         # [print(line) for line in map]
    #         continue

    # while(tmp_pos != pos):
    #     map[tmp_pos[0]][tmp_pos[1]] = map[tmp_pos[0]-dir[0]][tmp_pos[1]-dir[1]]
    #     tmp_pos = tmp_pos[0]-dir[0], tmp_pos[1]-dir[1]
    # map[pos[0]][pos[1]] = "."
    # pos = pos[0]+dir[0],pos[1]+dir[1]

    # print(move)
    # [print(line) for line in map]

res = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] != "[":
            continue
        res += 100*i+j
print(res)

