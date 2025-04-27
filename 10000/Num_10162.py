'''
- 최소단위인 10초로 나뉘어 떨어지지 않으면 불가능하므로 -1 출력
- 큰 값부터 나눠서 계산
'''

T = int(input())

if T % 10 != 0:
    print(-1)
else:
    Acount = T // 300
    Bcount = T % 300 // 60
    Ccount = T % 300 % 60 // 10

    print(Acount, Bcount, Ccount)
