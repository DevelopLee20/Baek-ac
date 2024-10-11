import sys

N = int(sys.stdin.readline())

for num in range(N):
    sentense = sys.stdin.readline().rstrip()
    print(f"{num+1}. {sentense}")
