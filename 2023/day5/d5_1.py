f = open("day5/input.txt", "r")
lines = f.read().splitlines()

_, seeds = lines[0].split(":")
seeds = [int(n) for n in seeds.split()]

steps = []

def init_steps():
    i = 3
    while True:
        step = []
        steps.append(step)
        while lines[i] != "":
            step.append([int(n) for n in lines[i].split()])
            i+=1
            if(i == len(lines)):
                return
        i+=2

init_steps()

for step_id in range(len(steps)):
    for i, seed in enumerate(seeds):
        for range in steps[step_id]:
            if seed >= range[1] and seed <= range[1]+range[2]:
                seeds[i]+=range[0]-range[1]
                break

print(min(seeds))