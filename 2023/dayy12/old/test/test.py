from itertools import combinations
n = 10
# .?????????? 2,2
len_groups = [3,2]
n_groups = len(len_groups)
n_empty = n-(n_groups-1)-sum(len_groups)

opts = combinations(range(n_groups+n_empty), n_groups)
for j, opt in enumerate(opts):
    decal = 0
    print(opt,end=" ")
    res = ['░']*n
    for i in range(len(opt)):
        for _ in range(len_groups[i]):
            res[opt[i]+decal] = "▓"
            decal+=1
    print("".join(res))
print(j)