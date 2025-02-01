import sys

N = int(sys.stdin.readline())
w_list = []
for i in range(N):
    w = int(sys.stdin.readline())
    w_list.append(w)

w_max = 0
for idx, w in enumerate(sorted(w_list)):
    value = (N - idx) * w
    w_max = max(w_max, value)

print(w_max)
