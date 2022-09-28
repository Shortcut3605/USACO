f = open("speeding.in","r")
w = open("speeding.out","w")

N, M = map(int, f.readline().strip().split())
limits = []
driving = []
for i in range(N):
    length, limit = map(int, f.readline().strip().split())
    for j in range(length):
        limits.append(limit)
for i in range(M):
    length, speed = map(int, f.readline().strip().split())
    for j in range(length):
        driving.append(speed)
maxOver = 0
for i in range(101):
    maxOver = max(maxOver, driving[i]-current[i])
print(maxOver, file=w)
f.close()
w.close()