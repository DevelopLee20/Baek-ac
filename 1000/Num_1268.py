'''
N번 학생 - 1학년~5학년
1~9반

1 -> 2, 3, 4, 5 확인
2 -> 3, 4, 5 확인
3 -> 4, 5 확인
n번째는 n+1 ~ N까지 확인
'''
import sys

N = int(sys.stdin.readline())
data = []
count = []
for n in range(N):
    line = [i for i in sys.stdin.readline().rstrip().split()]
    data.append(line)
    count.append([0 for _ in range(N)])

for x in range(N):
    for ax in range(x+1, N):
        for grade in range(5):
            if count[x][ax] != 0:
                break
            if data[x][grade] == data[ax][grade]:
                count[x][ax] = 1
                count[ax][x] = 1
                break

maxValue = sum(count[0])
maxIdx = 0
for idx in range(1, N):
    value = sum(count[idx])
    if maxValue < value:
        maxValue = value
        maxIdx = idx

print(maxIdx + 1)
