import re
with open("dayy12/input.txt") as f:
    lines = f.read().splitlines()

def gen_possibilities(record: str, patern: str):
    stack = set()
    res = set()
    stack.add((record, record.count('?')))
    while(len(stack) > 0):
        rec, i = stack.pop()
        if not is_matching(patern, rec):
            continue
        if i == 0: 
            res.add(rec)
            continue
        stack.add((rec.replace('?','.',1),i-1))
        stack.add((rec.replace('?','#',1),i-1))
    return res

def is_matching(patern, s):
    return re.match(patern, s) != None

lines = [[a, b.split(',')] for line in lines for a,b in [line.split()]]

res = 0
for i, line in enumerate(lines):
    print(f"line {i+1}/{len(lines)}\r",end="")
    record = "?".join(5*[line[0]])
    nbs = 5*line[1]
    l = len(record)

    paterns = [r'[#?]{'+n+r'}' for n in nbs]
    patern = r"^[\.?]*" + r"[\.?]+".join(paterns) + r"[\.?]*$"
    combins = [combin for combin in gen_possibilities(record, patern)]
    # print(len(combins))
    # print(combins)
    res+=len(combins)
print("\n",res,sep="")
