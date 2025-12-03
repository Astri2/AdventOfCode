with open("d2/input.txt") as f:
    lines = f.read().splitlines()

ids = lines[0].split(",")

res = 0

for idRange in ids:
    rangeBegin, rangeEnd = map(int, idRange.split("-"))
    for i in range(rangeBegin, rangeEnd+1):
        s = str(i)
        
        # odd length => can't be a repetition
        if(len(s) % 2 != 0): continue

        l = len(s)

        if(s[:l//2] == s[l//2:]): 
            print("invalid:", i)
            res += i
print(res)