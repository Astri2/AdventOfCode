f = open("day3/input.txt", "r")
lines = f.read().splitlines()

map = [list(line) for line in lines]
maxI = len(map)-1
s = 0

def getnumber(map, i, j):
    res = ""
    while(j>=0 and map[i][j].isnumeric()):
        j-=1
    j+=1
    while(j <= maxI and map[i][j].isnumeric()):
        res+=map[i][j]
        j+=1
    return int(res), (i, j)

def add_gear_number(map, i, j, numbers, numbers_loc):
    n, loc = getnumber(map, i, j)
    if not loc in numbers_loc:
        numbers_loc.add(loc)
        numbers.append(n)

def get_gear(map, i, j):
    numbers = []
    numbers_loc = set()
    if(i != 0):
        if(map[i-1][j].isnumeric()): 
            add_gear_number(map, i-1, j, numbers, numbers_loc)
        if(j != 0 and map[i-1][j-1].isnumeric()): 
            add_gear_number(map, i-1, j-1, numbers, numbers_loc)
        if(j != maxI and map[i-1][j+1].isnumeric()): 
            add_gear_number(map, i-1, j+1, numbers, numbers_loc)
    if(i != maxI):
        if(map[i+1][j].isnumeric()): 
            add_gear_number(map, i+1, j, numbers, numbers_loc)
        if(j != 0 and map[i+1][j-1].isnumeric()): 
            add_gear_number(map, i+1, j-1, numbers, numbers_loc)
        if(j != maxI and map[i+1][j+1].isnumeric()): 
            add_gear_number(map, i+1, j+1, numbers, numbers_loc)
    if(j != 0 and map[i][j-1].isnumeric()): 
        add_gear_number(map, i, j-1, numbers, numbers_loc)
    if(j != maxI and map[i][j+1].isnumeric()): 
        add_gear_number(map, i, j+1, numbers, numbers_loc)
    
    if(len(numbers) == 2):
        return numbers[0]*numbers[1]
    if(len(numbers) > 2):
        print("ERREUR")
        return -1
    return 0


s = 0
for i, line in enumerate(map):
    for j, tile in enumerate(line):
        if tile == "*":
            s += get_gear(map, i, j)
print(s)