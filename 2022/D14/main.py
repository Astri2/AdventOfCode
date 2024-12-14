TESTING = False

import numpy
from PIL import Image
from PIL.Image import Image as Im
from code_obscure import save_transparent_gif

def export(frames: list[Im]):
    save_transparent_gif(frames,1,"D14/frames/try.gif")
    # for i in range(len(frames)):
    #     frames[i].save(f"D14/frames/{i}.png")
#     im1 = Image.open('a.png')
# im2 = Image.open('b.png')
# im3 = Image.open('c.png')
# im1.save("out.gif", save_all=True, append_images=[im2, im3], duration=100, loop=0)

def print_m(m):
    mm = numpy.zeros(m.shape)
    for i in range(len(m)):
        for j in range(len(m[i])):
            mm[i,j] = 255 if m[i,j] == "#" else 0
    im = Image.fromarray(numpy.uint8(mm), 'L')
    return im

def print_sand(m,i,j):
    alpha_mask = numpy.zeros(m.shape)
    alpha_mask[i,j] = 255
    im_a = Image.fromarray(numpy.uint8(alpha_mask),mode="L")

    im_arr = numpy.zeros((*numpy.shape(m), 3), dtype=numpy.uint8)
    im_arr[i,j] = [200,200,0]
        
    im = Image.fromarray(numpy.uint8(im_arr), mode="RGB")
    im.putalpha(im_a)
    
    return(im)

def parse(lines):
    points = []
    depth = 1
    for line in lines:
        corner = line.split(" -> ")
        j,i = (int(n) for n in corner[0].split(","))
        depth = max(depth, i)
        for k in range(1,len(corner)):
            j_p,i_p = (int(n) for n in corner[k].split(","))

            depth = max(depth, i_p+1)

            minJ = min(j, j_p)
            minI = min(i, i_p)
            if i != i_p:
                points += [(minI+di,j) for di in range(abs(i-i_p)+1)]
            else: 
                points += [(i,minJ+dj) for dj in range(abs(j-j_p)+1)]
            j, i = j_p, i_p
    
    m = numpy.full((depth+2,2*(depth+1)+1),'.')
    
    spawn = (0, depth+1)
    m[spawn] = 'x'
    
    for point in points:
        m[point[0], point[1]-500+spawn[1]] = '#'
    m[-1] = '#'
    print_m(m)
    return m, spawn

def part1(content, lines):
    m, spawn = parse(lines)
    frames = [print_m(m)]
    r=0
    done = False
    while not done:
        if r == 60:
            pass
        i,j = spawn
        unit_done = False
        while not unit_done:
            # if i:
            #     done = unit_done = True
            if m[i+1][j] == '.':
                i+=1
            elif m[i+1][j-1] == '.':
                i+=1
                j-=1
            elif m[i+1][j+1] == '.':
                i+=1
                j+=1
            elif m[i][j] == 'x':
                r+=1
                done = unit_done = True
            else: 
                r+=1
                m[i, j] = 'o'
                # print_sand(i,j)
                unit_done = True
        frames.append(print_sand(m,i,j))
    print(r)
    export(frames)
def main():
    import os 
    folder = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
    file = open(f"{folder}\\input{'_test' if TESTING else ''}.txt",'r')
    content = file.read()
    lines = content.splitlines()
    
    part1(content, lines)

if __name__ == "__main__":
    main()