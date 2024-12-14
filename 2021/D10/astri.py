import re

def day10(lines):
    p1 = re.compile(r"(\(|\[|\{|\<)")
    p2 = re.compile(r"(\(\)|\[\]|\{\}|\<\>)")
    corr_map = { ")":3,"]":57,"}":1197,">":25137}
    miss_map = { "(":1,"[":2,"{":3,"<":4}
    corr_score=0
    miss_scores=[]
    i=0
    chunks=[]
    while i < len(lines):
        line = lines[i]
        for c in line:
            if re.match(p1,c):
                chunks.append(c)
            else:
                if re.match(p2,chunks[-1]+c):
                    chunks.pop()
                else:
                    print(chunks[-1], "and",c,"are not compatible")
                    corr_score += corr_map[c]
                    lines.remove(line)
                    chunks=[]
                    i-=1
                    break
        score=0
        while(len(chunks)!=0):
            score=score*5 + miss_map[chunks[-1]]
            chunks.pop()
        if score!=0:miss_scores.append(score)
        i+=1
    print(corr_score)
    miss_scores.sort()
    print(miss_scores[(len(miss_scores)-1)//2])
    
if __name__=="__main__":
    f = open("AdventOfCode2021\\D10\\input.txt")
    lines = f.read().splitlines()
    day10(lines)