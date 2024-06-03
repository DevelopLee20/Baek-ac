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

        if key == "I":
            heapq.heappush(heapMax, -value)
            heapq.heappush(heapMin, value)
        # elif key == "D":
        else:
            if len(heap) > 0:
                if value == -1:
                    heapq.heappop(heap)
                # elif value == 1:
                else:
                    heap = [heapq.heappop(heap) for _ in range(len(heap))]
                    heap.pop()
    
    heap = [heapq.heappop(heap) for _ in range(len(heap))]

    if len(heap) == 0:
        print("EMPTY")
    else:
        print(heap[-1], heap[0])
