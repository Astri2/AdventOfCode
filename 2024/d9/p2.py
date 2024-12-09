# 7h50 -> 8h23
TEST = False
import os
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

def disp(files, size):
    arr = ['.'] * size
    for file in files:
        f_shift, f_len, f_id = file
        for i in range(f_shift, f_shift+f_len):
            arr[i] = str(f_id)
    print("".join(arr))


line = list(map(int, lines[0]))
tot_len = sum(line)

holes: list[tuple[int, int]] = []
files: list[tuple[int, int, int]] = []

file = True
file_counter = 0

shift = 0
for i,c in enumerate(line):
    if file:
        files.append((shift, c, file_counter))
        file_counter += 1
    else: 
        holes.append((shift, c))
    shift += c
    file = not file

# disp(files, tot_len)

for i_f in range(len(files)-1, -1, -1):
    print(f"{len(files)-i_f}/{len(files)}",end='\r')
    f_shift, f_len, f_id = files[i_f]
    for i_h in range(len(holes)):
        h_shift, h_len = holes[i_h]

        if f_shift < h_shift: break
        
        if h_len >= f_len:
            f_shift = h_shift
            h_shift += f_len
            h_len -= f_len
            
            files[i_f] = (f_shift, f_len, f_id)
            holes[i_h] = (h_shift, h_len)
            break

    # disp(files, tot_len)


res = 0
for file in files:
    f_shift, f_len, f_id = file
    for shift in range(f_shift, f_shift+f_len):
        res += shift * f_id

print(res)
