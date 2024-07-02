'''
N (1, 2, 3, 4, 5, 6, 7)
계속 빼다가 남은 수가 i보다 작으면 종료
S = 1 -> N = 1
S = 3 -> N = 2
S = 6 -> N = 3
S = 200
200 - 1
199 - 2 ? ㅇㅋ
1 > maxN
'''

S = int(input())
maxN = 1
while (S - maxN) > maxN:
    S -= maxN
    maxN += 1

print(maxN)
