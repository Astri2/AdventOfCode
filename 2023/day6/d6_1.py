f = open("day6/input.txt", "r")
lines = f.read().splitlines()

times = [int(n) for n in lines[0].split(":")[1].split()]
dists = [int(n) for n in lines[1].split(":")[1].split()]

res = 1
for i in range(len(times)):
    time = times[i]
    dist = dists[i]
    wins = 0

    for press in range(0, time+1):
        if press*(time-press) > dist: 
            print(f"race {i}, {press} = win")
            wins+=1
    res *= wins
print(res)
