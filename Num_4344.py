for _ in range(int(input())):
    b,*a = list(map(int,input().split()))
    count = 0

    for i in a:
        if sum(a)/b < i:
            count += 1
    
    print('%0.3f%%' % float(count/int(b)*100))