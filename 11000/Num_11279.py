from heapq import heappop, heappush
import sys

heap = []
def push(x: int):
    heappush(heap, -x)

def pop():
    if len(heap) == 0:
        print(0)
    else:
        value = heappop(heap)
        print(-value)

N = int(input())
for _ in range(N):
    value = int(sys.stdin.readline())

    if value == 0:
        pop()
    else:
        push(value)
