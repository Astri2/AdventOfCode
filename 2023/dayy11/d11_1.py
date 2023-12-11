f = open("dayy11/input.txt", "r")
map = [line for line in f.read().splitlines()]
stars = list()
f.close()


def expandString(s, c, i):
    return s[:i] + c + s[i:]

def addColumn(i):
    for j, line in enumerate(map):
        map[j] = expandString(line, '.', i)

def addLine(i, emptyLine):
    map.insert(i, emptyLine)

def expand():
    x = 0
    while x < len(map[0]):
        empty = True
        for y in range(len(map)):
            if map[y][x] == '#':
                empty = False
        if(empty):
            addColumn(x)
            x+=1
        x+=1

    emptyLine = '.'*len(map[0])
    y=0
    while y < len(map):
        if map[y] == emptyLine:
            addLine(y, emptyLine)
            y+=1
        y+=1

def get_stars():
    for y in range(len(map)):
        for x in range(len(map[y])):
            if(map[y][x] == '#'):
                stars.append((x,y))

def print_map():
    print(*map,sep="\n")
    print(stars)

def compute_min_distances():
    res=0
    for i,star1 in enumerate(stars):
        for star2 in stars[i+1:]:
            res += abs(star1[0]-star2[0])+abs(star1[1]-star2[1])
    print(res)

expand()
get_stars()
print_map()
compute_min_distances()
            