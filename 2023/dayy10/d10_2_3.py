with open("dayy10/expanded.txt",'r') as f:
    map = [[[c] for c in list(line)] for line in f.read().splitlines()]

def rec(x, y):
    points = {(x,y)}
    s = 0
    inside = True
    while len(points) > 0:
        x,y = points.pop()
        if not map[y][x][0] in ",.": continue
        if map[y][x][0] == ".": s+=1
        map[y][x] = chars[-1]
        
        if(x > 0): points.add((x-1,y))
        else: inside = False
        if(y > 0): points.add((x,y-1))
        else: inside = False
        if(x < len(map[y])-1): points.add((x+1,y))
        else: inside = False
        if(y < len(map)-1): points.add((x,y+1))
        else: inside = False
    if not inside: chars[-1][0] = " "
    return s if inside else 0
    
chars = []
def cout_inside_tiles():
    res = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x][0] in ".,":
                chars.append(["#"])
                res+=rec(x, y)
    print(res)

cout_inside_tiles()
with open("dayy10/done.txt",'w') as f:
    print("\n".join(["".join([c[0] for c in line]) for line in map]),file=f)