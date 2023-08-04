# 못함

import math

for i in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r3 = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if r1+r2 == r3:
        print(1)
    elif r1+r2 < r3 or r3 == 0 and r1 != r2:
        print(0)
    elif r1+r2 > r3:
        print(2)
    elif r3 == 0 and r1 == r2:
        print(-1)