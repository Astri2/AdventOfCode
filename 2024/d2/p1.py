with open("d2/in.txt") as f:
    lines = f.read().splitlines()

safes = 0
for line in lines:
    nbs = list(map(int, line.split()))
    safe = True
    decreasing = True if nbs[1] < nbs[0] else False
    for i in range(1, len(nbs)):
        nb1 = nbs[i-1]; nb2 = nbs[i]
        
        if nb1 == nb2 or abs(nb1 - nb2) > 3:
            safe = False
            break
        if (decreasing and nb2 > nb1) or ((not decreasing) and nb2 < nb1):
            safe =  False
            break
    if safe:
        # print("safe")
        safes+=1
    # else: print("unsafe")
print(safes)
