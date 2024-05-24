'''
x1, y1, x2, y2
0 ~ N-1
0 <= N < N까지
'''

import sys

input = sys.stdin.readline

graph = []
N = int(input())
for _ in range(N):
    line = [int(i) for i in input().rstrip().split()]
    graph.append(line)

def rectBlue(x1, y1, x2, y2):
    for x in range(x1, x2):
        for y in range(y1, y2):
            if graph[x][y] != 1:
                return False
    
    return True

def rectWhite(x1, y1, x2, y2):
    for x in range(x1, x2):
        for y in range(y1, y2):
            if graph[x][y] != 0:
                return False
    
    return True

queue = [(0, 0, N, N)]
bluePaperCount = 0
whitePaperCount = 0
while len(queue):
    x1, y1, x2, y2 = queue.pop(0)

    if rectBlue(x1, y1, x2, y2):
        bluePaperCount += 1
    elif rectWhite(x1, y1, x2, y2):
        whitePaperCount += 1
    else:
        one = (x1, y1, (x1+x2) // 2, (y1+y2) // 2)
        two = (x1, (y1+y2) // 2, (x1+x2) // 2, y2)
        three = ((x1+x2) // 2, y1, x2, (y1+y2) // 2)
        four = ((x1+x2) // 2, (y1+y2) // 2, x2, y2)
        queue.append(one)
        queue.append(two)
        queue.append(three)
        queue.append(four)

print(whitePaperCount)
print(bluePaperCount)
