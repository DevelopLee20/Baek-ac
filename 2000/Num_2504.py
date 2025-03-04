# 스택 알고리즘
def peek(stack: list):
    if stack:
        return stack[-1]
    return 0

def push(stack: list, value):
    stack.append(value)

def pop(stack: list):
    if stack:
        return stack.pop()
    return -1

# 빈 스택 선언
stack = []
check = []

# 입력
string = input()

# 입력값 반복
for i in string:
    # 열린 괄호 처리
    if i == "(" or i == "[":
        push(stack, i)
        push(check, i)
        continue
    
    # )를 처리할 때
    elif i == ")":
        # 사전 상태 확인
        if peek(check) != "(":
            print(0)
            exit(0)
        else:
            pop(check)

        # 괄호 찾아서 반복
        number = 0
        while peek(stack) != "(":
            value = pop(stack)
            number += value
        
        pop(stack)
        number = max(2, number * 2)
        push(stack, number)

    # ]를 처리할 때
    elif i == "]":
        # 사전 상태 확인
        if peek(check) != "[":
            print(0)
            exit(0)
        else:
            pop(check)

        # 괄호 찾아서 반복
        number = 0
        while peek(stack) != "[":
            value = pop(stack)
            number += value
        
        pop(stack)
        number = max(3, number * 3)
        push(stack, number)

result = 0
for i in stack:
    if type(i) is not int:
        print(0)
        exit(0)
    result += i

print(result)
