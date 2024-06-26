n = int(input())

for x1 in range(int(n**0.5) + 1):
    for x2 in range(int((n-x1*x1)**0.5) + 1):
        for x3 in range(int((n-x1*x1-x2*x2)**0.5) + 1):
            for x4 in range(int((n-x1*x1-x2*x2-x3*x3)**0.5) + 1):
                if x4 > 0:
                    if x1**2 + x2**2 + x3**2 + x4**2 == n:
                        print((x1 != 0) + (x2 != 0) + (x3 != 0) + (x4 != 0))
                        exit(0)
