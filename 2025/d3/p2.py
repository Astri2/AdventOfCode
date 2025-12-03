with open("d3/input.txt") as f:
    lines = f.read().splitlines()

res = 0
for line in lines:

    best = 0
    begin_idx = 0
    end_idx_shift = 11
    for k in range(12):
        max_idx = -1
        max = -1

        for i in range(begin_idx, len(line)-end_idx_shift):
            c = line[i]
            if(int(c) > max):
                max = int(c)
                max_idx = i
        
        begin_idx = max_idx+1
        end_idx_shift -= 1
        best = 10*best + max
    print(f"Jolt: {best}")
    res += best

print(res)
    