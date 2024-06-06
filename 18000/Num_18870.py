import sys
input = sys.stdin.readline

N = int(input())
numList = [i for i in map(int, input().split())]

dic = {}
for idx, num in enumerate(sorted(set(numList))):
    dic[num] = idx

print(*[dic[num] for num in numList])
