class Seed:
    def __init__(self, begin, len):
        self.begin = begin
        self.len = len
        self.end = begin+len-1
        

    def __repr__(self) -> str:
        return f"Seed({self.begin}, {self.len})"


class Filter:
    def __init__(self, dest_begin, src_begin, len):
        self.dest_begin = dest_begin
        self.src_begin = src_begin
        self.len = len
        self.src_end = src_begin+len-1
        self.dest_end = dest_begin+len-1
        self.shift = dest_begin-src_begin

    def __repr__(self) -> str:
        return f"Filter({self.src_begin}, {self.len})"
        
f = open("day5/input.txt", "r")
lines = f.read().splitlines()

_, seeds = lines[0].split(":")
seeds = [int(n) for n in seeds.split()]
seeds: list[Seed] = [Seed(seeds[i],seeds[i+1]) for i in range(0, len(seeds), 2)]

print(seeds)
print(f"nb seeds : {sum([seed.len for seed in seeds])}")

steps: list[list[Filter]] = []

def init_steps():
    i = 3
    while True:
        step = []
        steps.append(step)
        while lines[i] != "":
            values = [int(n) for n in lines[i].split()]
            step.append(Filter(values[0], values[1], values[2]))
            i+=1
            if(i == len(lines)):
                return
        i+=2

init_steps()

for step_id, step in enumerate(steps):
    to_add = []
    for f_id, f in enumerate(step):
        s_id = 0
        while s_id < len(seeds):
            s = seeds[s_id]
            s_id+=1
            if s.end < f.src_begin or s.begin > f.src_end:
                continue
            
            if s.begin < f.src_begin and s.end > f.src_end: # out out
                # print(f"changing seed {s_id} at step {step_id} out out")
                seeds.append(Seed(s.begin, f.src_begin-s.begin)) # nouvelle range avant
                seeds.append(Seed(f.src_end+1, s.end-f.src_end)) # nouvelle range apres
                to_add.append(Seed(f.dest_begin, f.len)) # range au milieu et -> dest)
                seeds.remove(s)
                s_id-=1
                
            elif s.begin >= f.src_begin and s.end <= f.src_end: # in in
                # print(f"changing seed {s_id} at step {step_id} in in")
                to_add.append(Seed(s.begin+f.shift, s.len))
                seeds.remove(s)
                s_id-=1
                
            elif s.begin < f.src_begin and f.src_begin <= s.end <= f.src_end: # out in
                # print(f"changing seed {s_id} at step {step_id} out in")
                seeds.append(Seed(s.begin, f.src_begin-s.begin))
                to_add.append(Seed(f.dest_begin, s.end-f.src_begin+1))
                seeds.remove(s)
                s_id-=1
                
            elif f.src_end >= s.begin >= f.src_begin and s.end > f.src_end: # in out
                # print(f"changing seed {s_id} at filter {f_id} at step {step_id} in out")
                to_add.append(Seed(s.begin+f.shift, f.src_end-s.begin+1))
                seeds.remove(s)
                s_id-=1
                seeds.append(Seed(f.src_end+1, s.end-f.src_end))
                
            else: print("problem!")
    seeds += to_add    
    print(f"at the end of step {step_id}, we've got {len(seeds)} seed range")

print(f"nb seeds : {sum([seed.len for seed in seeds])}")
seeds = sorted(seeds, key=lambda s: s.begin)
print(f"lowest seed: {seeds[0]}")
