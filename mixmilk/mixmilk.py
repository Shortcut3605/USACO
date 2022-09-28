f = open("mixmilk.in", "r")
w = open("mixmilk.out", "w")

c1,m1 = map(int, f.readline().strip().split())
c2,m2 = map(int, f.readline().strip().split())
c3,m3 = map(int, f.readline().strip().split())

def pour(m1, c2, m2):
    if m1 + m2 <= c2:
        m2 += m1
        m1 = 0
        return m1, m2
    m1 = m1 + m2 - c2
    m2 = c2
    return m1, m2

for i in range(33):
    m1, m2 = pour(m1, c2, m2)
    m2, m3 = pour(m2, c3, m3)
    m3, m1 = pour(m3, c1, m1)
m1, m2 = pour(m1, c2, m2)

print(m1, file=w)
print(m2, file=w)
print(m3, file=w)

f.close()
w.close()