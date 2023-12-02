f = open("day2/input.txt",'r')

MAX_R = 12
MAX_G  = 13
MAX_B = 14

def play_game_part1(line) -> int:
    id, sets = line.split(":")
    _, id = id.split()
    sets = sets.split(";")
    for set in sets:
        set = set.split(",")
        for cube in set:
            n, color = cube.split()
            n = int(n)
            if(color == "blue" and n > MAX_B):
                return 0
            if(color == "red" and n > MAX_R):
                return 0
            if(color == "green" and n > MAX_G):
                return 0
    return int(id)

def play_game_part2(line):
    _, sets = line.split(":")
    sets = sets.split(";")
    max_r, max_g, max_b = (0,0,0)
    for set in sets:
        set = set.split(",")
        for cube in set:
            n, color = cube.split()
            n = int(n)
            if(color == "red"):
                max_r = max(max_r, n)
            if(color == "green"):
                max_g = max(max_g, n)
            if(color == "blue"):
                max_b = max(max_b, n)
    return (max_r*max_g*max_b)

lines = f.read().splitlines()
print(sum([play_game_part1(line) for line in lines]))
print(sum([play_game_part2(line) for line in lines]))
