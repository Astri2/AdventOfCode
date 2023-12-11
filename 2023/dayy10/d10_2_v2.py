# 8H02
test = False
if test: f = open("dayy10/input_test2.txt", "r")
else: f = open("dayy10/input.txt", "r")    

map = [[[c,False] for c in line] for line in f.read().splitlines()]
f.close()

def init_s():
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x][0] == 'S':
                return (x,y)
            
def move(x, y, last):
    tile = map[y][x][0]
    map[y][x][1]=True

    match tile:
        case '|': return (x,y-1,'n') if last == 'n' else (x, y+1,'s')
        case '-': return (x+1,y,'e') if last == 'e' else (x-1, y,'w')
        case 'L': return (x+1,y,'e') if last == 's' else (x, y-1,'n')
        case 'J': return (x-1,y,'w') if last == 's' else (x, y-1,'n')
        case '7': return (x-1,y,'w') if last == 'n' else (x, y+1,'s')
        case 'F': return (x+1,y,'e') if last == 'n' else (x, y+1,'s')
        case '.': return (-1,-1,'')

def travel():
    x, y = init_s()
    # look at input to guess first possible move
    if test:
        map[y][x][1] = ('F',True)
        dir='s'; y+=1
    else:
        map[y][x] = ('J',True)
        dir = 'n'; y-=1
    ###
    while(not map[y][x][1]):
        x, y, dir = move(x, y, dir)

def clear():
    for y in range(len(map)):
        for x in range(len(map[y])):
            if not map[y][x][1]:
                map[y][x] ="."
            else: map[y][x] = map[y][x][0]

def is_inside(x, y):
    s = 0
    while(x > 0):
        x-=1
        if map[y][x] in "|F7":
            s+=1
    return s%2

def fill(x, y, c):
    stack = {(x,y)}
    res = 0
    while len(stack) != 0:
        x, y = stack.pop()
        if map[y][x] != '.': continue
        map[y][x] = c
        res+=1
        if(x > 0): stack.add((x-1,y))
        if(x < len(map[y])-1): stack.add((x+1,y))
        if(y > 0): stack.add((x,y-1))
        if(y < len(map)-1): stack.add((x,y+1))
    return res

def count_inside():
    res = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if(map[y][x] == '.'):
                if is_inside(x,y):
                    res+=fill(x, y, '#')
                else: fill(x, y, ' ')
    print(res)

def print_map():
    s = ""
    for line in map:
        for t in line:
            s+=t[0]
        s+="\n"
    with open("dayy10/v2.txt", 'w') as f:
        f.write(s)

travel()
clear()
count_inside()
print_map()
