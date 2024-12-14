TESTING = True

def gen_set(n,m):
    return set(range(n,m+1))

def part2(content, lines):
    score = 0
    for line in lines:
        e1,e2 = line.split(",")
        s1 = gen_set(*[int(n) for n in e1.split("-")])
        s2: set = gen_set(*[int(n) for n in e2.split("-")])
        if s2.intersection(s1):
            score+=1
    print(score)

def part1(content, lines):
    # score = 0
    # for line in lines:
    #     e1,e2 = line.split(",")
    #     s1 = gen_set(*[int(n) for n in e1.split("-")])
    #     s2: set = gen_set(*[int(n) for n in e2.split("-")])
    #     if s2.issubset(s1) or s2.issuperset(s1):
    #         score+=1
    # print(score)

    print(sum([1 if pair[1].issubset(pair[0]) or pair[0].issubset(pair[1]) else 0 for pair in [[[l(*[int(n) for n in r.split("-")]) for r in splitted] for splitted in [line.split(",") for line in open("D4\\input.txt",'r').read().splitlines()]] for l in [lambda x,y : set(range(x,y+1))]][0]]))

if __name__ == "__main__":
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    content = file.read()
    lines = content.splitlines()
    
    part1(content, lines)
    # part2(content, lines)

    '''
    5-9,1-5
    2-7,1-3
    '''

    '''
    [["5-9,1-5"],["2-7,1-3"]]
    '''

    '''
    [[["5-9"],["1-5"]],[["2-7"],["1-3"]]]
    '''
    
    '''
    [[{5,6,7,8,9},{1,2,3,4,5}],[{2,3,4,5,6,7},{1,2,3}]]
    '''

    '''
    [1,1]
    '''

    '''
    2
    '''

    # r ="5-9"
    # print()