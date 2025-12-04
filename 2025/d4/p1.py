with open("d4/input.txt") as f:
    lines = f.read().splitlines()

map = []

# load map with padding
map.append(["."] * (len(lines[0])+2))
for line in lines: map.append(["."] + list(line) + ["."])
map.append(["."] * (len(lines[0])+2))

res = 0
for i in range(1, len(map)-1):
    for j in range(1, len(map[i])-1):
        if(map[i][j] != "@"): continue
        nb = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if(di == dj == 0): continue
                if map[i+di][j+dj] == "@": nb+=1
        if(nb < 4): 
            res+=1

print(res)