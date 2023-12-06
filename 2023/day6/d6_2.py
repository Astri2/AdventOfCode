f = open("day6/input.txt", "r")
lines = f.read().splitlines()

time = int(lines[0].split(":")[1].replace(" ",""))
dist = int(lines[1].split(":")[1].replace(" ",""))

i, j = 0, time
while(i*(time-i) < dist): i+=1
while(j*(time-j) < dist): j-=1
print(j-i+1)
