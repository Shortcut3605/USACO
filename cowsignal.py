from fileinput import close


f = open("cowsignal.in","r")
w = open("cowsignal.out","w")
m,n,k = f.readline().split()
m = int(m)
n = int(n)
k = int(k)

for i in range(m):
    line = f.readline().strip()
    for j in range(k):
        for z in line:
            print(z * k, end="",file=w)
        print("",file=w)

f.close()
w.close()