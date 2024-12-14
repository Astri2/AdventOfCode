TESTING = False

# import sys, io

# old = sys.stdout
# sys.stdout = r = io.StringIO()

def sum_coords(p1, p2):
    return (p1[0]+p2[0],p1[1]+p2[1])


def print_rope(rope,vis):
    m = [["." for _ in range(50)] for _ in range(50)]
    m[25][25] = "S"
    for v in vis:
        m[25+v[1]][25+v[0]] = "#"
    for i in range(len(rope)-1,-1,-1):
        m[25+rope[i][1]][25+rope[i][0]] = str(i) if i != 0 else 'H'
    for line in m[::-1]:
        for c in line:
            print(c,end="")
        print()
    print()

def print_mat(visited_places):
    m = [["." for _ in range(50)] for _ in range(50)]
    for c in visited_places:
        m[25+c[1]][25+c[0]] = "#"
    for line in m[::-1]:
        for c in line:
            print(c,end="")
        print()

def part2(content, lines):
    rope_length = 10

    directions = {'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}
    rope = [(0,0) for _ in range(rope_length)]
    visited_places = set()
    visited_places.add((0,0))
    for line in lines:
        # print(line)
        if line.startswith("R 17"):
            pass
        direction, dist = line.split()
        direction = directions[direction]
        dist: int = int(dist)

        for _ in range(dist):
            rope[0] = sum_coords(rope[0],direction)
            for i in range(1,len(rope)):
                if not(abs(rope[i-1][0]-rope[i][0]) <= 1 and abs(rope[i-1][1]-rope[i][1]) <= 1):
                    if(rope[i-1][0] == rope[i][0] or rope[i-1][1] == rope[i][1]):
                        sum = sum_coords(rope[i-1],rope[i])
                        rope[i] = (sum[0]//2,sum[1]//2)
                    else:
                        dir = (1 if rope[i-1][0] > rope[i][0] else -1,
                                    1 if rope[i-1][1] > rope[i][1] else -1)
                        rope[i] = sum_coords(rope[i],dir)
            visited_places.add(rope[-1])
            # print(len(visited_places))
            # print_rope(rope,visited_places)
    print(len(visited_places))
    # print_mat(visited_places) 


def part1(content, lines):
    directions = {'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}
    H_pos, T_pos = (0,0),(0,0)
    visited_places = set()
    visited_places.add((0,0))
    for line in lines:
        direction, dist = line.split()
        dist: int = int(dist)
        for _ in range(dist):
            H_pos = sum_coords(H_pos,directions[direction])
            if not(abs(H_pos[0]-T_pos[0]) <= 1 and abs(H_pos[1]-T_pos[1]) <= 1):
                if(H_pos[0] == T_pos[0] or H_pos[1] == T_pos[1]):
                    T_pos = sum_coords(T_pos,directions[direction])
                else:
                    dir = (1 if H_pos[0] > T_pos[0] else -1, 1 if H_pos[1] > T_pos[1] else -1)
                    T_pos = sum_coords(T_pos,dir)
                visited_places.add(T_pos)
    print(len(visited_places))


def main():
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    content = file.read()
    lines = content.splitlines()
    
    part1(content, lines)
    part2(content, lines)


if __name__ == "__main__":
    main()