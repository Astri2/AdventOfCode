with open("dayy18/input.txt",'r') as f:
    lines = f.read().splitlines()

minX, maxX, x = 0,0,0
minY, maxY, y = 0,0,0

for i,line in enumerate(lines):
    dir, n, color = line.split()
    n = int(n)
    color = color[2:-1]
    lines[i] = dir,n,color
    
    match dir:
        case "L":
            x-=n
            if x < minX : minX = x
        case "R":
            x+=n
            if x > maxX : maxX = x
        case "U":
            y-=n
            if y < minY : minY = y
        case "D":
            y+=n
            if y > maxY : maxY = y
print(minX, maxX)
print(minY, maxY)

map = [['.' for _ in range(maxX-minX+1)] for _ in range(maxY-minY+1)]

i,j = -minY, -minX

deltas = {"U":(-1,0), "D":(1,0), "L":(0,-1), "R":(0,1)}
for line in lines:
    dir, n, color = line
    di, dj =  deltas[dir]
    for r in range(1, n+1):
        i+=di
        j+=dj
        map[i][j] = "#"

# print("\n".join(["".join(line) for line in map]))


def explore(tile):
    stack = {tile}
    res = 0
    out = False
    while len(stack) > 0:
        i,j = stack.pop()
        if i < 0 or j < 0 or i == len(map) or j == len(map[0]):
            out = True
            continue
        if(map[i][j] == '.'):
            res+=1
            map[i][j] = ','
            stack.add((i+1,j))
            stack.add((i-1,j))
            stack.add((i,j+1))
            stack.add((i,j-1))
        elif(map[i][j] == '#'):
            continue
    return 0 if out else res

res = [0]
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == '#':
            res[0]+=1
        elif map[i][j] == ".":
            res[0]+=explore((i,j))
print(res)