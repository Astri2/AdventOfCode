# 8H02
test = False
if test:
    f = open("dayy10/input_test2.txt", "r")
else: f = open("dayy10/input.txt", "r")    

map = [[[c,False] for c in line] for line in f.read().splitlines()]

def init_s():
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x][0] == 'S':
                print (x,y)
                exit()
            
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
    
    # look at input to guess first possible move
    if test:
        x, y = 1, 1
        map[y][x][1] = True
        dir='s'; y+=1
    else:
        x, y = 109, 76
        map[y][x][1] = True
        dir = 'n'; y-=1
    ###
    while(not map[y][x][1]):
        x, y, dir = move(x, y, dir)

def clear():
    for y in range(len(map)):
        for x in range(len(map[y])):
            if not map[y][x][1]:
                map[y][x][0]="."


def print_map():
    s = ""
    for line in map:
        for t in line:
            s+=t[0]
        s+="\n"
    with open("dayy10/cleared.txt", 'w') as f:
        f.write(s)

travel()
clear()
print_map()
