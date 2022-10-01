f = open("blockgame.in","r")
w = open("blockgame.out","w")

blocks = []

N = int(f.readline().strip())
a = {}
alpha = 'a'
for i in range(0, 26):
    a[alpha] = 0
    alpha = chr(ord(alpha) + 1)
    



