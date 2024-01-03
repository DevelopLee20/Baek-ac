'''
수 입력 N, B
seed = B
seed가 B를 계속 곱했을 때 커지기 전까지 연산
'''

role = {
    10:"A", 11:"B", 12:"C", 13:"D", 14:"E",
    15:"F", 16:"G", 17:"H", 18:"I", 19:"J",
    20:"K", 21:"L", 22:"M", 23:"N", 24:"O",
    25:"P", 26:"Q", 27:"R", 28:"S", 29:"T",
    30:"U", 31:"V", 32:"W", 33:"X", 34:"Y",
    35:"Z"
}
N, B = map(int, input().split())

seed = B

while seed * B < N:
    seed = seed * B

while N > B:
    value = 0
    
    while N > seed:
        N = N - seed
        value = value + 1
    
    if value > 9:
        value = role[value]
        
    print(value, end="")
    seed = seed / B

if N > 9:
    N = role[N]

print(N)
