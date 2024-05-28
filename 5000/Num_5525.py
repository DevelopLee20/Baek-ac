'''
N = Pn -> 3, 5, 7
M = 입력(S)의 길이
S = 입력

시작 I = 1, O = 0
O 다음 I => +1, O 다음 O => 0
I 다음 O => +1, I 다음 I => 1
목표(2N+1) 달성시 2N-1로 초기화
'''

N = int(input())
M = int(input())
S = [i for i in input()]

patternIdx = 0
if S[0] == 'I':
    S[0] = 1
    patternIdx += 1
else:
    S[0] = 0

count = 0
pattern = "IO"
patternSize = 2 * N + 1
for idx in range(1, M):
    if S[idx] == pattern[patternIdx % 2]:
        S[idx] = S[idx-1] + 1
        patternIdx += 1
    elif S[idx] == 'O':
        S[idx] = 0
        patternIdx = 0
    else: # S[idx] == 'I'
        S[idx] = 1
    
    if S[idx] == patternSize:
        S[idx] = patternSize - 2
        count += 1

print(count)
