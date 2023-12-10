# 19min
# 8H02
f = open("dayy10/input.txt", "r")
map = [line for line in f.read().splitlines()]

def init_s():
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'S':
                return (x,y)
            
def move(x, y, last):
    tile = map[y][x]
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
    print(x, y)
    step = 1
    # look at input to guess first possible move
    dir = 'n' 
    y-=1
    ###
    while(map[y][x] != 'S'):
        x, y, dir = move(x, y, dir)
        step+=1
    print(step//2)

travel()
