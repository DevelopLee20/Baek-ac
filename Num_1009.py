for _ in range(int(input())):
    a,b = map(int,input().split())
    num = a**b % 10
    if num == 0:
        print(10)
    else:
        print(num)