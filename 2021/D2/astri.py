def get_pos(tab):
    posX=0
    posY=0
    aim=0
    for k in tab:
        if k[0] == "up": 
            posY-=k[1]
        elif k[0] == "down": 
            posY+=k[1]
        else: 
            posX+=k[1]
    return posX*posY

def get_new_pos(tab):
    posX=0
    posY=0
    aim=0
    for k in tab:
        print(k)
        if k[0] == "down": 
            aim+=k[1]
        elif k[0] == "up": 
            aim-=k[1]
        else: 
            posX+=k[1]
            posY+=aim*k[1]
    return posX*posY

def main():
    file = open("AdventOfCode2021\\D2\\input.txt",'r')
    lines = file.readlines()
    tab=[]
    for k in lines:
        s = k.split(" ",1)
        tab.append((s[0],int(s[1][0])))
    print(get_pos(tab))
    print(get_new_pos(tab))

if __name__ == "__main__":
    main()