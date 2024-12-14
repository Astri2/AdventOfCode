import re

def get_best_shoot(goal):
    xmin,xmax,ymin,ymax = goal
    best_shoot=(0,0)
    best_height=0
    for i in range(xmax+1):
        for k in range(3000):
            dx,dy=i,k
            x,y=0,0
            max_height=0
            while(x <= xmax and y >= ymin):
                x+=dx
                dx+= 1 if dx < 0 else -1 if dx > 0 else 0
                y+=dy
                dy-=1
                if dy == 0:
                    max_height = max(max_height,y)
                if(xmin <= x <= xmax and ymin <= y <= ymax):
                    if max_height > best_height:
                        best_height=max_height
                        best_shoot=(i,k)
    print("best height:",best_height,"for shoot:",best_shoot)


if __name__ == "__main__":
    f = open("AdventOfCode2021\\D17\\input.txt")
    goal = [int(k) for k in re.findall(r"-?[0-9]+",f.read())]
    get_best_shoot(goal)