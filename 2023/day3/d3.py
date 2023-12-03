f = open("day3/input.txt", "r")
lines = f.read().splitlines()

map = [list(line) for line in lines]
maxI = len(map)-1
s = 0

def getnumber(map, i, j):
    res = ""
    while(j <= maxI and map[i][j].isnumeric()):
        res+=map[i][j]
        j+=1
    return int(res), len(res)

def is_surounded_by_symbol(map, i, j):
    if(i != 0):
        if( not map[i-1][j] in "1234567890."): 
            return True
        if(j != 0 and not map[i-1][j-1] in "1234567890."): 
            return True
        if(j != maxI and not map[i-1][j+1] in "1234567890."): 
            return True
    if(i != maxI):
        if(not map[i+1][j] in "1234567890."): 
            return True
        if(j != 0 and not map[i+1][j-1] in "1234567890."): 
            return True
        if(j != maxI and not map[i+1][j+1] in "1234567890."): 
            return True
    if(j != 0 and not map[i][j-1] in "1234567890."): 
        return True
    if(j != maxI and not map[i][j+1] in "1234567890."): 
        return True

def is_part_number(map, i, j, l):
    for k in range(l):
        if(is_surounded_by_symbol(map, i, j+k)):
            return True
    return False
        
s = 0
for i, line in enumerate(map):
    j = 0
    while(j < len(line)):
        tile = map[i][j]
        if(tile.isnumeric()):
            n,l = getnumber(map, i, j)
            if(is_part_number(map, i, j, l)):
                s+=n
            j+=l-1
        j+=1
print(s)