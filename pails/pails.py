from typing import List


f = open("pails.in","r")
w = open("pails.out","w")


x = [False] * 1000
x,y,z = map(int,f.readline().strip().split())



def writeToOut(curr):
    global out
    global outlen
    if curr > out:
        out = curr
def solve(curr,lens):
    if x[curr]: return
    if curr+x>z:
        x[curr] = True
        writeToOut(curr)
        return
    elif curr+x == z:
        writeToOut(curr+x)
    if curr+y<=z:
        solve(curr+y,lens+1)
    solve(curr+x,lens+1)
        
solve(0,0)
print(out,file=w)
f.close()
w.close()