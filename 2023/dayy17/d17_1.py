import sys
sys.setrecursionlimit(2000)

with open("dayy17/input_test.txt",'r') as f:
    map = f.read().splitlines()


min_dists = {}
min_dists[(0,0,'u',3)] = 0
min_dists[(0,0,'d',3)] = 0
min_dists[(0,0,'l',3)] = 0
min_dists[(0,0,'r',3)] = 0

def get_possible_moves(i,j,dir, forward_moves_left):
    moves = set()
    match dir:
        case 'u':
            if(i > 0 and forward_moves_left > 0): 
                moves.add((i-1,j,'u',forward_moves_left-1))
            if(j > 0): moves.add((i,j-1,'l',2))
            if(j < len(map)-1): moves.add((i,j+1,'r',2))
        case 'd':
            if(i < len(map)-1 and forward_moves_left > 0): 
                moves.add((i+1,j,'d',forward_moves_left-1)) 
            if(j > 0): moves.add((i,j-1,'l',2))
            if(j < len(map)-1): moves.add((i,j+1,'r',2))
        case 'l':
            if(j > 0 and forward_moves_left > 0): 
                moves.add((i,j-1,'l',forward_moves_left-1))
            if(i > 0): moves.add((i-1,j,'u',2))
            if(i < len(map)-1): moves.add((i+1,j,'d',2))
        case 'r':
            if(j < len(map)-1 and forward_moves_left > 0): 
                moves.add((i,j+1,'r',forward_moves_left-1))
            if(i > 0): moves.add((i-1,j,'u',2))
            if(i < len(map)-1): moves.add((i+1,j,'d',2))
    return moves

best = [99999999999]
def explore(i, j, dir, forward_left, dist, visited: set):
    if (i,j) in visited: return 99999999999
    visited.add((i,j))
    if dist > best[0]: return 99999999999
    for x in range(forward_left, 3):
        if min_dists.get((i,j,dir, x), 99999999999) < dist:
            return 99999999999
    min_dists[(i,j,dir,forward_left)]=dist
    
    if (i,j) == (len(map)-1, len(map)-1): return dist
    
    moves = get_possible_moves(i,j,dir,forward_left)
    min_dist = 99999999999
    for move in moves:
        # moves.add((i,j+1,'r',forward_moves_left-1))
        move_dist = explore(*move, dist+int(map[move[0]][move[1]]), visited.copy())
        min_dist = min(min_dist, move_dist)
    if best[0] > min_dist:
        print("found new min:",min_dist)
        best[0] = min_dist
    return min_dist

a = explore(0,0,'r',3,0,set())
print(a)
print(best[0])