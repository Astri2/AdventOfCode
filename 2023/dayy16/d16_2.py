with open("dayy16/input.txt",'r') as f:
    mmap = [[[t,[]] for t in line] for line in f.read().splitlines()]

begins = [(0,j,'d') for j in range(len(mmap[0]))]+\
    [(len(mmap)-1,j,'u') for j in range(len(mmap[0]))]+\
    [(i,0,'r') for i in range(len(mmap))]+\
    [(i,len(mmap[0])-1,'l') for i in range(len(mmap))]
# print(len(begins))

max_res = [0]
for id,begin in enumerate(begins):
    print(id)
    map = [[[t[0],[]] for t in line] for line in mmap]
    next_stack: set = {begin}
    res = [0]
    while True:
        if(len(next_stack) == 0): break
        stack = next_stack.copy()
        next_stack = set()
        while len(stack) > 0:
            i, j, dir = stack.pop()
            if not -1 < i < len(map): continue
            if not -1 < j < len(map[0]): continue
            if dir in map[i][j][1]: continue

            if len(map[i][j][1])==0: res[0]+=1
            map[i][j][1].append(dir)
            match map[i][j][0]:
                case ".": 
                    match dir:
                        case "r": next_stack.add((i,j+1,'r'))
                        case "l": next_stack.add((i,j-1,'l'))
                        case "u": next_stack.add((i-1,j,'u'))
                        case "d": next_stack.add((i+1,j,'d'))
                case "-": 
                    match dir:
                        case "r": next_stack.add((i, j+1, 'r'))
                        case "l": next_stack.add((i, j-1, 'l'))
                        case "u" | "d":
                            next_stack.add((i, j-1, 'l'))
                            next_stack.add((i, j+1, 'r'))
                case "|":
                    match dir:
                        case "u": next_stack.add((i-1, j, 'u'))
                        case "d": next_stack.add((i+1, j, 'd'))
                        case "l" | "r":
                            next_stack.add((i-1, j, 'u'))
                            next_stack.add((i+1, j, 'd'))
                case "/":
                    match dir:
                        case "u": next_stack.add((i, j+1, 'r'))
                        case "d": next_stack.add((i, j-1, 'l'))
                        case "r": next_stack.add((i-1, j, 'u'))
                        case "l": next_stack.add((i+1, j, 'd'))
                case "\\":
                    match dir:
                        case "u": next_stack.add((i, j-1, 'l'))
                        case "d": next_stack.add((i, j+1, 'r'))
                        case "r": next_stack.add((i+1, j, 'd'))
                        case "l": next_stack.add((i-1, j, 'u'))
    # if begin == ()
    max_res[0] = max(max_res[0], res[0])
print(max_res[0])
# print("\n".join(["".join(['#' if t[1] else '.' for t in line]) for line in map]))