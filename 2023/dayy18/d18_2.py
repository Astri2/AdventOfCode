with open("dayy18/input_test.txt",'r') as f:
    lines = f.read().splitlines()

minX, maxX, x = 0,0,0
minY, maxY, y = 0,0,0

dirs = ["R","D","L","U"]
for i,line in enumerate(lines):
    dir, n, color = line.split()
    color = color[2:-1]
    # dir = dirs[int(color[-1])]
    # n = int(color[:-1], 16)
    n = int(n)
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

i,j = -minY, -minX
deltas = {"U":(-1,0), "D":(1,0), "L":(0,-1), "R":(0,1)}
vertices = []
for line in lines:
    dir, n, color = line
    di, dj =  deltas[dir]
    i += di*n
    j += dj*n
    vertices.append((i,j))

print(vertices)

map = [["." for _ in range(7)] for _ in range(10)]

res = 0
# vertices = [(0,0),(1,0),(1,2),(3,2),(3,3),(0,3)]
for i in range(len(vertices)):
    # print("passe")
    res += (vertices[i-1][1]*vertices[i][0]-vertices[i][1]*vertices[i-1][0])
    map[vertices[i][0]][vertices[i][1]] = "#"

print(res//2)
print("\n".join(["".join(line) for line in map]))