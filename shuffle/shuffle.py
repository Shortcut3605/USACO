f = open("shuffle.in","r")
w = open("shuffle.out","w")

N = int(f.readline().strip())
keys = []
values = []
swaps = [0] * N
keys = f.readline().strip().split()
for i in range(len(keys)):
    keys[i] = int(keys[i]) 
values = f.readline().strip().split()
for i in range(3):
    for j in range(len(keys)):
        swaps[j] = values[keys[j]-1]
    values = swaps
    swaps = [0] * N
for j in values:
    print(j,file=w)


f.close()
w.close()