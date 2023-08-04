for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if c%a == 0:
        print(100*a+int(((c-0.1)//a)) + 1)
    else:
        print(100*(c%a)+int(((c-0.1)//a)) + 1)