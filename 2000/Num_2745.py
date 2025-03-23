'''
아스키 변환, A가 65 이므로 -55를 하면 10이 됨
'''
# 입력
B, N = input().split()
N = int(N)

# 10진법으로 변환
value = 0
for digit, b in enumerate(B[::-1]):
    try:
        value += int(b) * (N**digit)
    except:
        value += (ord(b)-55) * (N**digit)

print(value)
