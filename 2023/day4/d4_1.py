f = open("day4/input.txt", "r")
lines = f.read().splitlines()

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
from math import pow
s = 0
i=0
for line in lines:    
    _, nb = line.split(":")
    win, player = nb.split("|")
    win = set(win.split())
    player = set(player.split())

    matches = win.intersection(player)
    if len(matches) != 0:
        s+=2**(len(matches)-1)
print(s)
