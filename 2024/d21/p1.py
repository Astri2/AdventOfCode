TEST = False
import os
from PIL import Image
import numpy as np
with open(f"2024/{os.path.split(os.path.split(__file__)[0])[1]}/input{"_test" if TEST else ""}.txt") as f:
    lines = f.read().splitlines()

class Pad:
    def __init__(self, i, j, press):
        self.i = i
        self.j = j
        self.press = press

EXPORT = True
mask = np.asarray(Image.open("2024/d21/mask.png"))
alphabet = np.asarray(Image.open("2024/d21/alphabet.png"))
bin_mask = mask[:,:,3] == 255
BG = (10, 30, 0, 255)
SELECT = (30, 90, 0, 255)
PRESS = (60, 175, 0, 255)
F = 4 # expanding factor
images: list[Image.Image] = []
def draw(r1: Pad, r2: Pad, r3: Pad, h: Pad, sim_name: str, frame_id: int, to_write: str):
    sels = np.full(mask.shape, BG)
    
    sels[F*1  + F*8*r1.i : F*8  + F*8*r1.i, F*1  + F*8*r1.j : F*8  + F*8*r1.j] = PRESS if r1.press else SELECT
    sels[F*1  + F*8*r2.i : F*8  + F*8*r2.i, F*28 + F*8*r2.j : F*35 + F*8*r2.j] = PRESS if r2.press else SELECT
    sels[F*19 + F*8*r3.i : F*26 + F*8*r3.i, F*28 + F*8*r3.j : F*35 + F*8*r3.j] = PRESS if r3.press else SELECT
    if h.press:
        sels[F*36 + F*8*h.i  : F*43 + F*8*h.i,  F*28 + F*8*h.j  : F*35 + F*8*h.j]  = PRESS
    
    for j, c in enumerate(to_write):
        
        if c.isalpha(): id = ord(c)-65
        elif c.isnumeric(): id = int(c)+26
        else: print("oskour")
        
        letter = alphabet[F*4*id: F*4 + F*4*id, 0:F*3]
        
        # sels[F*40 : F*44, F*6 + F*4*j : F*6 + F*4*(j+1)] = letter
        sels[F*40 : F*44, F*6 + F*4*j : F*9 + F*4*j] = letter
    
    sels = sels.astype(np.uint8)
    
    sels[bin_mask] = mask[bin_mask]
    
    img = Image.fromarray(sels)
    images.append(img)
    # img.save(f"2024/d21/imgs/{sim_name}_{frame_id}.png")

def export(root: str, sim_name: str):
    images[0].save(f"{root}/{sim_name}.gif", save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)

token_to_pos1 = {
    "7": (0,0), "8": (0,1), "9": (0,2),
    "4": (1,0), "5": (1,1), "6": (1,2),
    "1": (2,0), "2": (2,1), "3": (2,2),
                "0": (3,1), "A": (3,2)
}
pos1_to_token = {
    (0,0): "7", (0,1): "8", (0,2): "9",
    (1,0): "4", (1,1): "5", (1,2): "6",
    (2,0): "1", (2,1): "2", (2,2): "3",
                (3,1): "0", (3,2): "A"
}
 
token_to_pos2 = {
                "^": (0,1), "A": (0,2),
    "<": (1,0), "v": (1,1), ">": (1,2)
}
pos2_to_token = {
               (0,1): "^", (0,2): "A",
    (1,0):"<", (1,1):"v" , (1,2): ">"
}

token_to_dir = {
    "^": (-1,0), ">": (0,1), "v": (1,0), "<": (0,-1)
}

    
def get_r1_path(i1, j1, i2, j2):
    if i1 == i2:
        return ("<" if j1 > j2 else ">")*abs(j1-j2)
    if j1 == j2:
        return ("^" if i1 > i2 else "v")*abs(i1-i2)
    
    res = ""
    if i1 == 3:
        res += "^"
        i1-=1
        res += ("^" if i1 > i2 else "v")*abs(i1-i2)
        i1 = i2
        
    if j1 == 0:
        res += ">"
        j1+=1
        res += ("<" if j1 > j2 else ">")*abs(j1-j2)
        j1 = j2
        
    res += ("^" if i1 > i2 else "v")*abs(i1-i2)
    res += ("<" if j1 > j2 else ">")*abs(j1-j2)
    
    return res

def get_r2_path(i1, j1, i2, j2):
    if i1 == i2:
        return ("<" if j1 > j2 else ">")*abs(j1-j2)
    if j1 == j2:
        return ("^" if i1 > i2 else "v")*abs(i1-i2)
    
    res = ""
    if i1 == 0:
        res+= "v"
        i1+=1
        res += ("^" if i1 > i2 else "v")*abs(i1-i2)
        i1 = i2
        
    if j1 == 0:
        res +=">"
        j1+=1
        res += ("<" if j1 > j2 else ">")*abs(j1-j2)
        j1 = j2    
        
    res += ("^" if i1 > i2 else "v")*abs(i1-i2)
    res += ("<" if j1 > j2 else ">")*abs(j1-j2)
    
    return res

def main():
    res = 0
    
    for line in lines:
        images.clear()
        code = line
        
        robot1 = Pad(3,2,False)
        robot2 = Pad(0,2,False)
        robot3 = Pad(0,2,False)
        human = Pad(None, None, False)
        draw(robot1, robot2, robot3, human, code, 0, "")
        for _ in range(10): images.append(images[-1])
        human.press = True
                
        pos = token_to_pos1["A"]
        path1 = ""
        for c in code:
            new_pos = token_to_pos1[c]
            path1 += get_r1_path(*pos, *new_pos) + "A"
            pos = new_pos

        path2 = ""
        pos = token_to_pos2["A"]
        for c in path1:
            new_pos = token_to_pos2[c]
            path2 += get_r2_path(*pos, *new_pos) + "A"
            pos = new_pos
        
        path3 = ""
        pos = token_to_pos2["A"]
        for c in path2:
            new_pos = token_to_pos2[c]
            path3 += get_r2_path(*pos, *new_pos) + "A"
            pos = new_pos
        res += len(path3)*int(code[:3])
        
        if not EXPORT: continue
        
        to_print = ""
        for frame_id, c in enumerate(path3):
            robot3.press = False
            robot2.press = False
            robot1.press = False
            human.i, human.j = token_to_pos2[c]
            
            if c == "A":
                robot3.press = True
                if pos2_to_token[(robot3.i, robot3.j)] == "A":
                    robot2.press = True
                    if pos2_to_token[(robot2.i, robot2.j)] == "A":
                        robot1.press = True
                        to_print += pos1_to_token[(robot1.i, robot1.j)]
                    else:
                        di, dj = token_to_dir[pos2_to_token[(robot2.i, robot2.j)]]
                        robot1.i += di
                        robot1.j += dj
                else:
                    di,dj = token_to_dir[pos2_to_token[(robot3.i, robot3.j)]]
                    robot2.i += di
                    robot2.j += dj
            else:
                di, dj = token_to_dir[c]
                robot3.i += di
                robot3.j += dj
            
            draw(robot1, robot2, robot3, human, code, frame_id+1, to_print)
        
        for _ in range(10): images.append(images[-1])
        print(code)
        export("2024/d21/imgs", code)
        
    print(res)    

if __name__ == "__main__":
    main()
    