'''
() 끼리 짝 이루기
[] 끼리 짝 이루기
문자열도 균형이 잡혀있어야 한다. -> 의미가 없는 것 같다.
문장의 마지막은 . 으로 종료
내용이 공백일 때도 yes로 간주 -> 기본 값은 yes 이다.
내용이 . 만 받아지면 종료
'''
import sys

input = sys.stdin.readline

while True:
    string = input()

    if string[0] == ".":
        break

    stack = []; output = "yes"

    for i in string:
        if i == ".":
            if len(stack) != 0:
                output = "no"
            break

        if i == "[":
            stack.append(i)
        elif i == "]":
            if len(stack) > 0:
                if stack.pop() != "[":
                    output = "no"
                    break
            else:
                output = "no"
                break
        elif i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) > 0:
                if stack.pop() != "(":
                    output = "no"
                    break
            else:
                output = "no"
                break

    print(output)
