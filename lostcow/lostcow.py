f = open("lostcow.in", "r")
w = open("lostcow.out","w")

x,y = map(int, f.readline().strip().split())
ct = 1
prevct = 0
dir = 1
dist = 0
while True:
    newct = ct * dir;
    for i in range(ct):
        dist += 1
        x += dir
        if x == y:
            print(i,file=w)
    ct *= 2
    dist += 1
    dir *= -1
    

f.close()
w.close()