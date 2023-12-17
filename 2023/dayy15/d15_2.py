from functools import lru_cache

with open("dayy15/input.txt", 'r') as f:
    steps = f.read().split(',')

@lru_cache(maxsize=None)
def calc_code(step, s):
    if not step: return s
    s += ord(step[0])
    s*=17
    s%=256
    return calc_code(step[1:],s)

boxes = [[] for _ in range(256)]
lengths = {}

res = 0
for step in steps:
    # print(step)
    if step[-1] == '-':
        prefix = step[:-1]
        s=calc_code(prefix, 0)
        if prefix in boxes[s]:
            boxes[s].remove(prefix)
    else:
        prefix = step[:-2]
        l = int(step[-1])
        s=calc_code(prefix, 0)
        if not prefix in boxes[s]:
            boxes[s].append(prefix)
        lengths[prefix] = l

# print(boxes)
# print(lengths)
res = 0
for i, box in enumerate(boxes):
    for j, focal in enumerate(box):
        res += (i+1)*(j+1)*lengths[focal]
print(res)