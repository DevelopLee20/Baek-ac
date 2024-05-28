'''
정수 배열 계산 언어 AC
R: 뒤집기
D: 첫번째 수 버리기, 비어있는데 D 사용시 에러 발생
에러 발생시 error 출력
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    nList = eval(input().rstrip())

    front = 0
    end = n
    count = 0
    error = False
    for fun in p:
        if fun == 'R':
            count += 1
        if fun == 'D':
            if n == 0:
                error = True
                break
            else:
                if count % 2 == 0:
                    front += 1
                else:
                    end -= 1
                n -= 1

    if error:
        print("error")
    elif n:
        if count % 2 == 0:
            print(str(nList[front:end]).replace(" ", ""))
        else:
            print(str(nList[front:end][::-1]).replace(" ", ""))
    else:
        print("[]")
