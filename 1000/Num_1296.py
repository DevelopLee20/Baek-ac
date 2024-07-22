'''
L의 개수
O의 개수
V의 개수
E의 개수
'''
import sys

input = sys.stdin.readline

L = 0
O = 0
V = 0
E = 0

for i in input():
    if i == 'L':
        L += 1
    elif i == 'O':
        O += 1
    elif i == 'V':
        V += 1
    elif i == 'E':
        E += 1

percent = -1
name = ""

N = int(input())
for _ in range(N):
    nL = L
    nO = O
    nV = V
    nE = E

    nName = input().rstrip()
    for i in nName:
        if i == 'L':
            nL += 1
        elif i == 'O':
            nO += 1
        elif i == 'V':
            nV += 1
        elif i == 'E':
            nE += 1

    per = ((nL+nO) * (nL+nV) * (nL+nE) * (nO+nV) * (nO+nE) * (nV+nE)) % 100


    if per > percent:
        percent = per
        name = nName
    
    if per == percent:
        name = sorted([name, nName])[0]

print(name)
