'''
SK 기준
n 차례에서 승리하려면
n-1에서 져야함
n-3에서 져야함
'''
N = int(input())

SKWinList = [False] * (N+1)

if N >= 1:
    SKWinList[1] = True
if N >= 3:
    SKWinList[3] = True

for i in range(4, N+1):
    if not SKWinList[i-3] and not SKWinList[i-1]:
        SKWinList[i] = True

if SKWinList[N]:
    print("SK")
else:
    print("CY")
