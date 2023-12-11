# 55min
f = open("dayy11/input.txt", "r")
map = [[1 if t == '.' else -1 for t in line] for line in f.read().splitlines()]
stars = list()
f.close()
EXPENSION_RATE=1_000_000

def editColumn(i):
    for j in range(len(map)):
        map[j][i] = EXPENSION_RATE

def editLine(i):
    map[i] = [EXPENSION_RATE]*len(map)

def expand():
    x = 0
    while x < len(map[0]):
        empty = True
        for y in range(len(map)):
            if map[y][x] == -1:
                empty = False
        if(empty):
            editColumn(x)
            x+=1
        x+=1

    y=0
    while y < len(map):
        if not -1 in map[y]:
            editLine(y)
            y+=1
        y+=1

def get_stars():
    for y in range(len(map)):
        for x in range(len(map[y])):
            if(map[y][x] == -1):
                stars.append((x,y))

def print_map():
    print(*map,sep="\n")
    print(stars)

def compute_min_distances():
    res=0        
    for i,star1 in enumerate(stars):
        for star2 in stars[i+1:]:
            dist = 0
            xdist = star2[0]-star1[0]
            xPosit = xdist > 0
            xdist += (1 if xPosit else -1)
            ydist = star2[1]-star1[1]
            yPosit = ydist > 0
            ydist += (1 if yPosit else -1)

            for dx in range(1 if xPosit else -1,xdist, 1 if xPosit else -1):
                dist+=abs(map[star1[1]][star1[0]+dx])
            for dy in range(1 if yPosit else -1, ydist, 1 if yPosit else -1):
                dist+=abs(map[star1[1]+dy][star1[0]+dx])
            res += dist
    print(res)

expand()
get_stars()
print_map()
compute_min_distances()
            