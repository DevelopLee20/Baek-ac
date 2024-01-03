for _ in range(int(input())):
    a = int(input())
    b = int(input())
    c = [x for x in range(1,b+1)]
    for __ in range(a):
        for i in range(len(c)-1):
            c[i+1] = c[i] + c[i+1]
    
    print(c[b-1])