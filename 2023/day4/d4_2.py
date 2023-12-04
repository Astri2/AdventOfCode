from math import pow

f = open("day4/input.txt", "r")
lines = f.read().splitlines()
card_count = [1]*len(lines)
s = 0
i=0
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53

while(i < len(lines)):
    line = lines[i]
    
    _, nb = line.split(":")
    win, player = nb.split("|")
    win = set(win.split())
    player = set(player.split())

    matches = win.intersection(player)
    for k in range(1, len(matches)+1):
        card_count[i+k]+=card_count[i]
    
    i+=1
print(sum(card_count))
