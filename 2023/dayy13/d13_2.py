IS_PART_1 = False

with open("dayy13/input.txt",'r') as f:
    str_input = f.read()

def calc_score(s1, s2):
    diff=0
    for c1, c2 in zip(s1, s2):
        diff+=(c1!=c2)
    return diff

def get_sym_axis(pattern):
    l_pattern = len(pattern)
    for i in range(l_pattern-1):
        delta = 0
        is_sym = True
        had_to_fix = IS_PART_1
        while(i-delta >= 0 and i+1+delta < l_pattern):
            score = calc_score(pattern[i-delta], pattern[i+1+delta])
            if score > 1:
                is_sym = False
                break
            if score == 1:
                if had_to_fix: 
                    is_sym = False
                    break
                else: had_to_fix = True
            # if(pattern[i-delta] != pattern[i+1+delta]):
            delta+=1
        if(is_sym and had_to_fix): 
            return i+1
    return -1

patterns = str_input.split("\n\n")
line_patterns = [pattern.split("\n") for pattern in patterns]
# print(line_patterns)
column_patterns = [["".join(pattern[i][j] for i in range(len(pattern))) for j in range(len(pattern[0])) ] for pattern in line_patterns]

res = 0
for line_pattern, column_pattern in zip(line_patterns, column_patterns):
    line_axis = get_sym_axis(line_pattern)
    column_axis = get_sym_axis(column_pattern)
    print(line_axis,column_axis)
    res += 100*line_axis if line_axis != -1 else column_axis
print(res)