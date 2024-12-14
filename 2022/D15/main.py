TESTING = False

import re

def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def part1(content, lines):
    line_id = 2000000
    beacons = set()
    impossible_pos = set()
    for line in lines:
        matches = re.findall("x=([\-0-9]+), y=([\-0-9]+)",line)
        xS, yS = (int(n) for n in matches[0])
        xB, yB = (int(n) for n in matches[1])
        
        beacons.add((xB,yB))

        distS_B = dist((xS,yS),(xB,yB))
        dy = abs(line_id - yS)

        [impossible_pos.add((xS+i, line_id)) for i in range(0,distS_B-dy+1)]
        [impossible_pos.add((xS-i, line_id)) for i in range(1,distS_B-dy+1)]

    impossible_pos = impossible_pos.difference(beacons)
    print(len(impossible_pos))

def main():
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    content = file.read()
    lines = content.splitlines()
    
    part1(content, lines)
            
if __name__ == "__main__":
    main()
