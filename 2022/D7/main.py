TESTING = True

import re
    
def gen_tree(lines: list[str], i):
    i+=1
    t = []
    w = 0
    while i < len(lines) and lines[i] != "$ cd ..":
        match = re.findall("[0-9]+",lines[i])
        if match:
            w+=int(match[0])
        if lines[i].startswith("$ cd"):
            tt,ww,i = gen_tree(lines,i)
            t.append((tt,ww))
            w+=ww
        i+=1
    return t, w, i

def get_tree(lines):
    return gen_tree(lines,0)[:2]

def sum_tree(t):
    sum = 0
    if t[1] <= 100_000:
        sum+=t[1]
    for folder in t[0]:
        sum+=sum_tree(folder)
    return sum

def del_tree(t):
    weights= [t[1]]
    for sub in t[0]:
        weights+=del_tree(sub)
    return weights

def part1(content, lines):
    i = 0
    tree = get_tree(lines)
    print(tree)
    print(sum_tree(tree)) # part 1
    ws = sorted(del_tree(tree))
    obj = tree[1] - 40_000_000
    
    for w in ws:
        if w >= obj:
            print(w)
            return

def main():
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    content = file.read()
    lines = content.splitlines()
    
    part1(content, lines)

if __name__ == "__main__":
    main()