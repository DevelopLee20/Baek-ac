'''
a -> 1, z -> 26
1221 -> (1+2+2+1) % M = H
H = sum(NumList) % M
H = sum(NumList * r^i) % M
r = 31
M = 1234567891
'''
r = 31
M = 1234567891

AlphaDict = {}
for i in range(26):
    AlphaDict[chr(ord('a') + i)] = i + 1

num = int(input())
NumList = [AlphaDict[i] for i in input()]

SumNumList = 0

for sqrt, i in enumerate(NumList):
    SumNumList += i * r**(sqrt)

print(SumNumList % M)
