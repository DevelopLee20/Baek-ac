import sys

a = int(sys.stdin.readline())
c = list(map(int,sys.stdin.readline().split()))

o = c[0]; o2 = c[0]

for i in range(1,len(c)):
    if c[i] > o:
        o = c[i]
    if c[i] < o2:
        o2 = c[i]

print("{} {}".format(o2,o))