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

res = 0
for step in steps:
    res+=calc_code(step, 0)
print(res)