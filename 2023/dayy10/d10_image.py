from PIL import Image

PART2 = True

with open("dayy10/done.txt",'r') as f:
    lines = f.read().splitlines()

im = Image.new(mode="RGB", size=(len(lines[0]), len(lines)))

for y in range(im.height):
    for x in range(im.width):
        if lines[y][x] in "#":
            im.putpixel((x,y), (255,255,255))
        elif lines[y][x] in " ":
            im.putpixel((x,y), (0, 0, 0) if PART2 else (255,255,255))
        elif lines[y][x] in "|-JL7F":
            im.putpixel((x,y), (255, 0, 0))
        else: im.putpixel((x,y), (0, 255, 0)) # shouldn't run

if(PART2): im.save("dayy10/image2.png","png")
else: im.save("dayy10/image1.png","png")