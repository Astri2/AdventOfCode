with open("dayy13/input.txt",'r') as f:
    str_input = f.read()

def get_sym_axis(pattern):
    l_pattern = len(pattern)
    for i in range(l_pattern-1):
        if(pattern[i] == pattern[i+1]):
            delta = 1
            is_sym = True
            while(i-delta >= 0 and i+1+delta < l_pattern):
                if(pattern[i-delta] != pattern[i+1+delta]):
                    is_sym = False
                    break
                delta+=1
            if(is_sym): 
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