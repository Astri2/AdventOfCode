with open("d2/input.txt") as f:
    lines = f.read().splitlines()

ids = lines[0].split(",")

res = 0

for idRange in ids:
    rangeBegin, rangeEnd = map(int, idRange.split("-"))
    for i in range(rangeBegin, rangeEnd+1):
        s = str(i)
        

        for j in range(1, len(s)//2+1):
            if s[j:].replace(s[:j], "") == "":
                print(f"invalid: {i}. Pattern is {s[j:]}")
                res += i
                break
        

        
print(res)