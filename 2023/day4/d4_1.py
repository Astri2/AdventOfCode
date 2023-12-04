f = open("day4/input.txt", "r")
lines = f.read().splitlines()

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
from math import pow
s = 0
i=0
while(i < len(lines)):
    line = lines[i]
    i+=1
    
    id, nb = line.split(":")
    _, id = id.split()
    id = int(id)-1
    win, player = nb.split("|")
    win = set(win.split())
    player = set(player.split())

    matches = win.intersection(player)
    for k in range(1, len(matches)+1):
        lines.append(lines[id+k])
print(len(lines))
