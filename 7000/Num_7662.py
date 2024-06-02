import heapq
import sys

input = sys.stdin.readline

T = int(input())
for t in range(T):
    k = int(input())
    heapMax = []
    heapMin = []

    for _ in range(k):
        key, value = input().split()
        value = int(value)

        if key == 'I':
            if value > 0:
                heapq.heappush(heapMax, -value)
            else:
                heapq.heappush(heapMin, value)
        else:
            if value == 1:
                if len(heapMax) > 0:
                    heapq.heappop(heapMax)
                elif len(heapMin) > 0:
                    heapq.heappop(heapMin)

            elif value == -1:
                if len(heapMin) > 0:
                    heapq.heappop(heapMin)
                elif len(heapMax) > 0:
                    heapq.heappop(heapMax)

    if len(heapMax) + len(heapMin) == 0:
        print("EMPTY")
    else:    
        if len(heapMax) > 0 and len(heapMin) == 0:
            outputMax = -heapMax[0]
            outputMin = outputMax
        elif len(heapMin) == 0 and len(heapMin) > 0:
            outputMin = heapMin[0]
            outputMax = outputMin
        else:
            outputMax = -heapMax[0]
            outputMin = heapMin[0]

        print(outputMax, outputMin)
