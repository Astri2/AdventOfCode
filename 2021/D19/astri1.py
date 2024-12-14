def locate_scanners(scanners):
    for i in range(len(scanners)):
        for k in range(i,len(scanners)):
            if i == k: continue
            s1 = scanners[i] ; s2 = scanners[k]
            diffs={}
            for b1 in s1:
                for b2 in s2:
                    diff = tuple([b1[j]-b2[j] for j in range(3)])
                    if diff in diffs.keys():
                        diffs[diff]+=1
                    else: diffs[diff]=1
            print()


if __name__ == "__main__":
    f = open("AdventOfCode2021\\D19\\input.txt")
    lines = f.read().splitlines()
    scanners=[] ; i=0
    for __ in range(2):
        if i!=0: i+=2    
        else: i+=1
        scanners.append([])
        while(i < len(lines) and lines[i]!=""):
            scanners[-1].append([int(coord) for coord in lines[i].split(",")])
            i+=1
    locate_scanners(scanners)