'''
x와 y의 최댓값, 최솟값을 찾은 후 넓이를 계산
입력이 많아질 수 있으므로 sys.stdin.readline() 사용
'''
import sys

# 입력
N = int(sys.stdin.readline())

xy_list = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())

    xy_list.append((x, y))

# 최댓값, 최솟값 계산
if N == 1:
    print(0)
else: # O(N)
    x_max = xy_list[0][0]
    y_max = xy_list[0][1]
    x_min = xy_list[0][0]
    y_min = xy_list[0][1]

    for x, y in xy_list[1:]:
        x_max = max(x, x_max)
        y_max = max(y, y_max)
        x_min = min(x, x_min)
        y_min = min(y, y_min)

    print((x_max-x_min)*(y_max-y_min))
