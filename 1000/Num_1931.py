import sys

input = sys.stdin.readline

N = int(input())
reservation = []
for _ in range(N):
    start, end = map(int, input().split())
    reservation.append([start, end])

reservation.sort(key = lambda x: (x[1], x[0]))

endTime = 0
count = 0
for start, end in reservation:
    if endTime <= start and endTime <= end:
        count += 1
        endTime = end

print(count)
