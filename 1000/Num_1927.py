import sys
import heapq

input = sys.stdin.readline

heap = []
N = int(input())
for _ in range(N):
    x = int(input())

    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            output = heapq.heappop(heap)
            print(output)
    else:
        heapq.heappush(heap, x)
