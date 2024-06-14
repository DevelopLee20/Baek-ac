import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    nDic = {}
    for _ in range(n):
        name, clothType = input().rstrip().split()

        if clothType not in nDic:
            nDic[clothType] = 1
        else:
            nDic[clothType] += 1

    count = 1
    for num in nDic.values():
        count *= (num + 1)

    print(count - 1)
