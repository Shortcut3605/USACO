f = open("blist.in","r")
w = open("blist.out","w")

N = int(f.readline().strip())

dropoff = [0] * 1000
pickup = [0] * 1000
maxT = 0
for i in range(N):
    s,t,b = f.readline().strip().split()
    s = int(s)
    t = int(t)
    b = int(b)
    dropoff[s-1] += int(b)
    pickup[t-1] += int(b)
    maxT = max(maxT, t-1)
maxBuckets = 0
bucketsOpen = 0
for i in range(maxT):
    bucketsOpen += pickup[i]
    if(bucketsOpen < dropoff[i]):
        diff = dropoff[i] - bucketsOpen
        maxBuckets += diff
        bucketsOpen = 0
    else:
        bucketsOpen -= dropoff[i]
    print(pickup[i],dropoff[i],bucketsOpen)

print(maxBuckets,file=w)
f.close()
w.close()