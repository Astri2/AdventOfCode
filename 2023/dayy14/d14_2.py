def cycle(map):
    # north
    # print("north")
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'O':
                k = i
                while(k > 0 and map[k-1][j] == '.'):
                    map[k][j] = '.'
                    map[k-1][j] = 'O'
                    k-=1
    # print("\n".join(["".join(line) for line in map]))
    # print("west")
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'O':
                k = j
                while(k > 0 and map[i][k-1] == '.'):
                    map[i][k] = '.'
                    map[i][k-1] = 'O'
                    k-=1
    # print("\n".join(["".join(line) for line in map]))
    # print("south")
    for i in range(len(map)-1, -1, -1):
        for j in range(len(map[i])):
            if map[i][j] == 'O':
                k = i
                while(k < (len(map)-1) and map[k+1][j] == '.'):
                    map[k][j] = '.'
                    map[k+1][j] = 'O'
                    k+=1
    # print("\n".join(["".join(line) for line in map]))
    # print("east")
    for i in range(len(map)):
        for j in range(len(map[i])-1, -1, -1):
            if map[i][j] == 'O':
                k = j
                while(k < (len(map[i])-1) and map[i][k+1] == '.'):
                    map[i][k] = '.'
                    map[i][k+1] = 'O'
                    k+=1
    # print("\n".join(["".join(line) for line in map]))

def score(map):
    res = 0
    for i, line in enumerate(map):
        res += (len(map)-i)*line.count('O')
    print(res)


cache_maps = list()
cache_maps_to_i = dict()
def handle_repetition(smap, i, N=1_000_000_000):
    previous = cache_maps_to_i[smap]
    offset = i-previous
    target = N%offset
    while target < previous: target+=offset
    print(f"cycle {i+1} is synced with cycle {previous+1}")
    print(f"offset is {offset}")
    print(f"target is {target}")
    target_map = cache_maps[target-1]
    score(target_map)

def copy(map):
    return [[t for t in line] for line in map]

def main():
    with open("dayy14/input.txt",'r') as f:
        map = [[tile for tile in line] for line in f.read().splitlines()]
    for i in range(1_000_000_000):
        cycle(map)
        smap = str(map)
        if map in cache_maps:
            handle_repetition(smap, i)
            return
        cache_maps.append(copy(map))
        cache_maps_to_i[smap] = i

main()