import numpy as np
from time import perf_counter

t = perf_counter()
SIZE = [0] # max id (computed while parsing)

f = open("day5/input.txt", "r")
lines = f.read().splitlines()

_, seeds = lines[0].split(":")
seeds = [int(n) for n in seeds.split()]

for i in range(0, len(seeds), 2):
    SIZE[0] = max(SIZE[0], seeds[i]+seeds[i+1])

class Filter:
    def __init__(self, dest_begin, src_begin, len):
        self.dest_begin = dest_begin
        self.src_begin = src_begin
        self.len = len
        self.src_end = src_begin+len-1
        self.dest_end = dest_begin+len-1
        self.shift = dest_begin-src_begin
steps: list[list[Filter]] = []
def init_steps():
    i = 3
    while True:
        step = []
        steps.append(step)
        while lines[i] != "":
            values = [int(n) for n in lines[i].split()]
            SIZE[0] = max(SIZE[0], values[1]+values[2])
            step.append(Filter(values[0], values[1], values[2]))
            i+=1
            if(i == len(lines)):
                return
        i+=2
init_steps()

map = np.zeros(SIZE[0], bool)
for i in range(0, len(seeds), 2):
    map[seeds[i]:seeds[i]+seeds[i+1]] = True

for step_id, step in enumerate(steps):
    print(f"begin step {step_id} (0/{len(step)} filters)",end="\r")
    mask = np.zeros(SIZE[0], bool)
    for filter_id, filter in enumerate(step):
        print(f"begin step {step_id} ({filter_id+1}/{len(step)} filters)",end="\r")
        mask[filter.dest_begin:filter.dest_end+1] = map[filter.src_begin:filter.src_end+1]
        # map[filter.src_begin:filter.src_end+1] = False
    print(f"\nbegin merge of step {step_id}")
    map = np.logical_xor(map, mask)

for i, location in enumerate(map):
    if location: 
        print(i)
        break
print(f"took {perf_counter()-t}s")