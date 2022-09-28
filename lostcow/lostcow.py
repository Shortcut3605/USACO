from pickle import FALSE


f = open("lostcow.in", "r")
w = open("lostcow.out","w")

x,y = map(int, f.readline().strip().split())
if x == y: 
    print(0, file=w)
    f.close()
    w.close()
    exit()
    
ct = 1
dir = 1
currX = x
dist = 0
for i in range(9):
    for j in range(currX, x+(ct*dir)+1, dir):
        dist += 1
        if(j == y):
            print(dist,file=w)
            f.close()
            w.close()
            exit()
    currX = x + (ct*dir)
    ct *= 2
    dir *= -1
    
print(9 * abs(x-y),file=w)
f.close()
w.close()