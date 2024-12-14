import re

def get_hit_counter(goal):
    xmin,xmax,ymin,ymax = goal
    hits=0
    for i in range(xmax+1):
        for k in range(ymin,3000):
            dx,dy=i,k
            x,y=0,0
            hit = False
            while(x <= xmax and y >= ymin and not hit):
                x+=dx
                dx+= 1 if dx < 0 else -1 if dx > 0 else 0
                y+=dy
                dy-=1
                if(xmin <= x <= xmax and ymin <= y <= ymax):
                   hits+=1
                   hit = True
    print("hits",hits)
    print(hit)


if __name__ == "__main__":
    f = open("AdventOfCode2021\\D17\\input.txt")
    goal = [int(k) for k in re.findall(r"-?[0-9]+",f.read())]
    get_hit_counter(goal)