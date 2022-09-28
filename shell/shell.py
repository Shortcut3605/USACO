f = open("shell.in","r")
w = open("shell.out", "w")


N = int(f.readline().strip())
swaps = []
for i in range(N):
    a, b, g = f.readline().strip().split()
    a = int(a)
    b = int(b)
    g = int(g)
    swaps.append([a,b,g])
currmax = -1
for i in range(3):
    shells = [-1, -1, -1]
    shells[i] = 1
    ct = 0
    for j in swaps:
        temp = shells[j[0]-1]
        shells[j[0]-1] = shells[j[1]-1]
        shells[j[1]-1] = temp
        if shells[j[2]-1] == 1:
            ct += 1
    currmax = max(currmax, ct)
print(currmax, file=w)
f.close()
w.close()