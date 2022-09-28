f = open("lostcow.in", "r")
w = open("lostcow.out","w")

x,y = map(int, f.readline().strip().split())
ct = 1
prevct = 0
dir = 1
while True:
    newct = ct * dir;
    for i in range(ct):
        x += dir
        if x == y:
            print(i,file=w)
    ct *= 2
    dir *= -1
    

f.close()
w.close()