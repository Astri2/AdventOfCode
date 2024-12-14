TESTING = True
import re

def part2(content, lines):
    i = 0
    stacks = [[] for __ in range((len(lines[0])+1)//4)]
    while not re.match(" 1.+",lines[i]):
        line = lines[i]
        k = 0
        while(k < len(line)):
            if(line[k]) == "[":
                stacks[k//4].insert(0,line[k+1])
            k+=4
        i+=1
    i+=2 #skip empty line
    print(stacks)
    while i < len(lines):
        operations, fromm, to = (int(n) for n in re.findall("[0-9]+",lines[i]))
        print('-->',lines[i])
        i+=1
        to_put = []
        for __ in range(operations):
            to_put.append(stacks[fromm-1].pop())
            print(stacks)
        to_put.reverse()
        stacks[to-1]+=to_put
    print("".join([stack[-1] for stack in stacks]))

def part1(content, lines):
    i = 0
    stacks = [[] for __ in range((len(lines[0])+1)//4)]
    while not re.match(" 1.+",lines[i]):
        line = lines[i]
        k = 0
        while(k < len(line)):
            if(line[k]) == "[":
                stacks[k//4].insert(0,line[k+1])
            k+=4
        i+=1
    i+=2 #skip empty line
    print(stacks)
    while i < len(lines):
        operations, fromm, to = (int(n) for n in re.findall("[0-9]+",lines[i]))
        print('-->',lines[i])
        i+=1
        for __ in range(operations):
            stacks[to-1].append(stacks[fromm-1].pop())
            print(stacks)
    print("".join([stack[-1] for stack in stacks]))

def one_line():
    [[[[print(a[i][-1],end="") for i in range(len(a))] for __ in [[[[l(a,nbs) for __ in range(int(nbs[0]))] for nbs in [__import__("re").findall("[0-9]+",line)]] for line in content.split("\n\n")[1].split("\n")] for l in [lambda a,nbs : (a[int(nbs[2])-1].append(a[int(nbs[1])-1].pop()),print(a))]]] for a in [[stack[::-1] for stack in [[[[inline[1+4*shift+k*line_size] for k in range(len(inline)//line_size) if inline[1+4*shift+k*line_size]!= ' '] for shift in range(3)] for line_size in [len(content.split("\n")[0])+1]] for inline in [" ".join([line for line in content.splitlines() if "[" in line])+" "]][0][0]]]] for content in [open(f"D5/input{'_test' if TESTING else ''}.txt",'r').read()]]


    # print(a)


if __name__ == "__main__":
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    # content = file.read()
    # lines = content.splitlines()
    
    # part1(content, lines)
    # part2(content, lines)
    one_line()