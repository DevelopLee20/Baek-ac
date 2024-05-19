'''
1번부터 N명의 사람이 앉아있음
K번째 사람 제거 pop()
'''

N, K = map(int, input().split())

circle = [str(i) for i in range(1, N+1)]

idx = K - 1
print("<", end="")
while len(circle) != 1:
    print(circle.pop(idx) + ",", end=" ")
    idx = (idx + K - 1) % len(circle)

print(circle[0] + ">")
