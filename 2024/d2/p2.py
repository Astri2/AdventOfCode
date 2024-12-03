with open("d2/in.txt") as f:
    lines = f.read().splitlines()

safes = 0
for line in lines:
    nbs_ = list(map(int, line.split()))

    for j in range(len(nbs_)):
        nbs = nbs_[:j] + nbs_[j+1:]

        safe = True
        decreasing = True if nbs[1] < nbs[0] else False
        for i in range(1, len(nbs)):
            nb1 = nbs[i-1]; nb2 = nbs[i]
            
            if nb1 == nb2 or abs(nb1 - nb2) > 3:
                safe = False
                break
            elif (decreasing and nb2 > nb1) or ((not decreasing) and nb2 < nb1):
                safe =  False
                break
        if safe: 
            safes+=1
            break
print(safes)
