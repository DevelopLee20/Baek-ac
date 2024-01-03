for i in range(int(input())):
    a,b = input().split()
    e = ''
    for i in b:
        e += i*int(a)
    print(e)