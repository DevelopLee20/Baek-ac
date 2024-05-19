'''
포켓몬 개수 N
맞춰야 하는 문제 개수 M
1 <= N, M N= 100,000
'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

doGam = {}
for number in range(1, N+1):
    name = input().rstrip()

    doGam[str(number)] = name
    doGam[name] = number

for _ in range(M):
    print(doGam[input().rstrip()])
