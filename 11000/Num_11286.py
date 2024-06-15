'''
절댓값힙
x != 0 push
x = 0 pop - 비었을 때 0 출력
          - 절댓값 가장 작은 값 출력
python의 heapq에서 (a, b)가 저장된다고 할 때, a를 기준으로 heap을 구현하는 방법?
'''
import heapq
import sys

N = int(sys.stdin.readline())
minHeap = []
for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(minHeap) == 0:
            print(0)
        else:
            value, sign = heapq.heappop(minHeap)

            if sign:
                print(value)
            else:
                print(-value)
    else:
        value = abs(x)
        sign = (x > 0)
        heapq.heappush(minHeap, (value, sign))
