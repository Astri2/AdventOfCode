with open("d5/input.txt") as f:
    lines = f.read().splitlines()

ranges = set()

i = 0
while True:
    line = lines[i] 
    i += 1
    if(line == ""): break

    ranges.add(tuple(map(int, line.split("-"))))

merged_ranges = []
for begin, end in sorted(ranges):
    if len(merged_ranges) != 0 and (merged_ranges[-1][1] >= begin - 1):
        merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], end))
    else: merged_ranges.append((begin, end))

res = 0
print(merged_ranges)
for begin, end in merged_ranges:
    res += 1 + (end - begin)
print(res)