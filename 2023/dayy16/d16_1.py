with open("dayy16/input_test.txt",'r') as f:
    map = [[[t,[]] for t in lines] for lines in f.read().splitlines()]

def main():
    stack: set = {(0,0,'r',0)}
    res = 0
    frames = dict()
    while len(stack) > 0:
        i, j, dir, depth = stack.pop()
        if not -1 < i < len(map): continue
        if not -1 < j < len(map[0]): continue
        if dir in map[i][j][1]: continue

        frames[depth] = frames.get(depth, [])+[(i,j)]
        if len(map[i][j][1])==0: 
            res+=1
        map[i][j][1].append(dir)
        match map[i][j][0]:
            case ".": 
                match dir:
                    case "r": stack.add((i,j+1,'r',depth+1))
                    case "l": stack.add((i,j-1,'l',depth+1))
                    case "u": stack.add((i-1,j,'u',depth+1))
                    case "d": stack.add((i+1,j,'d',depth+1))
            case "-": 
                match dir:
                    case "r": stack.add((i, j+1, 'r',depth+1))
                    case "l": stack.add((i, j-1, 'l',depth+1))
                    case "u" | "d":
                        stack.add((i, j-1, 'l',depth+1))
                        stack.add((i, j+1, 'r',depth+1))
            case "|":
                match dir:
                    case "u": stack.add((i-1, j, 'u',depth+1))
                    case "d": stack.add((i+1, j, 'd',depth+1))
                    case "l" | "r":
                        stack.add((i-1, j, 'u',depth+1))
                        stack.add((i+1, j, 'd',depth+1))
            case "/":
                match dir:
                    case "u": stack.add((i, j+1, 'r',depth+1))
                    case "d": stack.add((i, j-1, 'l',depth+1))
                    case "r": stack.add((i-1, j, 'u',depth+1))
                    case "l": stack.add((i+1, j, 'd',depth+1))
            case "\\":
                match dir:
                    case "u": stack.add((i, j-1, 'l',depth+1))
                    case "d": stack.add((i, j+1, 'r',depth+1))
                    case "r": stack.add((i+1, j, 'd',depth+1))
                    case "l": stack.add((i-1, j, 'u',depth+1))
    print(res)
    print(frames)
main()
