TESTING = False

from functools import cmp_to_key

def parse_line(line):
    # Edge case
    if line == '[]': return []
    
    els = []
    line = line[1:-1] # remove outer brackets
    begin_index = 0
    bracket_counter = 0
    for c in range(len(line)):
        if line[c] == "[":
            bracket_counter += 1
        elif line[c] == "]":
            bracket_counter -=1
        elif bracket_counter == 0 and line[c] == ",":
            els.append(line[begin_index:c])
            # we set the next element beging right after comas
            begin_index = c+1
    els.append(line[begin_index:len(line)])
    return[int(el) if el.isnumeric() else parse_line(el) for el in els]

def compare(el1, el2):
    if type(el1) == int:
        if type(el2) == int:
            return -1 if el1 < el2 else 0 if el1 == el2 else 1
        else:
            return compare_packet_couple([el1],el2)
    elif type(el2) == int:
        return compare_packet_couple(el1,[el2])
    else: 
        return compare_packet_couple(el1,el2)

def compare_packet_couple(l, r):
    if l == r:
        return 0
    for i in range(min(len(l),len(r))):
        s = compare(l[i],r[i])
        if s != 0 : return s
    return -1 if len(l) < len(r) else 1

def part2(content, lines):
    packets = [[[2]],[[6]]]
    for i in range(0,len(lines)+1,3):
        packets.append(parse_line(lines[i]))
        packets.append(parse_line(lines[i+1]))
    #Am too lazy to write a proper sort algorithm
    packets.sort(key=cmp_to_key(compare_packet_couple))

    print((1+packets.index([[2]]))*(1+packets.index([[6]])))

def part1(content, lines):
    score = 0
    packet_couples = []
    for i in range(0,len(lines)+1,3):
        packet_couples.append((parse_line(lines[i]), parse_line(lines[i+1])))
    
    for i in range(0,len(packet_couples)):
        if compare_packet_couple(packet_couples[i][0],packet_couples[i][1]) == -1:
            score+=i+1

    print(score)

def main():
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    content = file.read()
    lines = content.splitlines()
    
    part1(content, lines)
    part2(content, lines)

if __name__ == "__main__":
    main()
