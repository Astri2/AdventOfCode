import re
with open("dayy12/input.txt") as f:
    lines = f.read().splitlines()
lines = [[a, b.split(',')] for line in lines for a,b in [line.split()]]

def gen_possibilities(record: str):
    stack = set()
    res = set()
    stack.add((record, record.count('?')))
    while(len(stack) > 0):
        rec, i = stack.pop()
        if i == 0: 
            res.add(rec)
            continue
        stack.add((rec.replace('?','.',1),i-1))
        stack.add((rec.replace('?','#',1),i-1))
    return res

def is_matching(patern, s):
    return re.match(patern, s) != None


res = 0
for line in lines:
    record = line[0]
    nbs = line[1]
    l = len(record)

    paterns = [r'#{'+n+r'}' for n in nbs]
    patern = r"^\.*" + r"\.+".join(paterns) + r"\.*$"
    combins = [combin for combin in gen_possibilities(record) if is_matching(patern, combin)]
    # print(len(combins))
    # print(combins)
    res+=len(combins)
print(res)
