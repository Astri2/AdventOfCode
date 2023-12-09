#5min
f = open("day9/input_test.txt", "r")
res = 0

def extrapolate(seq):
    a = 0
    for seq_i in seq[::-1]:
        a= -a+seq_i[0]
    return a

for line in f.read().splitlines():
    seq = [list(map(int, line.split()))]
    while True:
        diff_seq = [0]*(len(seq[-1])-1)
        all0 = True
        for i in range(len(diff_seq)):
            diff =  seq[-1][i+1]-seq[-1][i]
            diff_seq[i] = diff
            if diff != 0: all0 = False
        if all0:
            res+=extrapolate(seq)
            break
        else: seq.append(diff_seq)
print(res)