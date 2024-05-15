'''
괄호를 지웠을 때 최소가 되는 값...
가능한 패턴 a b 
- + 패턴이면 a-(b+c)
- - 패턴이면 a b c
- 가 나오면 + 계속 나올 때까지 더해, 그리고 - 나오거나 종료되면 다 빼
그러면 스택으로 구현하는게 좋지 않을까?
'''

mathe = input()
result = 0
num = ''
minus = False

for char in mathe:
    if char == '-':
        if minus:
            result -= int(num)
        else:
            result += int(num)
            minus = True
        num = ''
    elif char == '+':
        if minus:
            result -= int(num)
        else:
            result += int(num)
        num = ''
    else:
        num += char

if minus:
    print(result - int(num))
else:
    print(result + int(num))
