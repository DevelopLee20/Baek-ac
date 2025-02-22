import heapq
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())

    heapMax = []
    heapMin = []
    visited = [False] * k
    for index in range(k):
        key, value = input().split()
        value = int(value)

        if key == "I":
            heapq.heappush(heapMax, (-value, index))
            heapq.heappush(heapMin, (value, index))
            visited[index] = True
        elif key == "D":
            if value == -1:
                while heapMin and not visited[heapMin[0][1]]:
                    heapq.heappop(heapMin)
                if heapMin:
                    visited[heapMin[0][1]] = False
                    heapq.heappop(heapMin)
            
            elif value == 1:
                while heapMax and not visited[heapMax[0][1]]:
                    heapq.heappop(heapMax)
                if heapMax:
                    visited[heapMax[0][1]] = False
                    heapq.heappop(heapMax)
    
    while heapMax and not visited[heapMax[0][1]]:
        heapq.heappop(heapMax)
    while heapMin and not visited[heapMin[0][1]]:
        heapq.heappop(heapMin)

    if not heapMin or not heapMax:
        print("EMPTY")
    else:
        print(-heapMax[0][0], heapMin[0][0])
