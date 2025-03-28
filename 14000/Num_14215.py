'''
가장 큰 값이 나머지 두 수의 합과 같아질 때까지 반복
'''
# 입력
a, b, c = map(int, input().split())

# 입력 변환 후 계산
number_list = sorted([a, b, c], reverse=True)

while number_list[0] >= (number_list[1] + number_list[2]):
    number_list[0] -= 1

print(sum(number_list))
