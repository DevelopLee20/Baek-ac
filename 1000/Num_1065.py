def solve():
    cnt = 0
    for i in range(1,int(input())+1):
        a = str(i)
        if len(a) < 3:
            cnt += 1
        elif len(a) == 3:
            if int(a[2]) + int(a[0]) == int(a[1])*2:
                print(i)
                cnt += 1
        else:
            if int(a[0])-int(a[1]) == int(a[1])-int(a[2]) == int(a[2])-int(a[3]):
                print(i)
                cnt += 1
    return cnt

print(solve())