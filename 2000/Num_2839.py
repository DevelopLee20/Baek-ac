a = int(input())

if(a-5*int((a-3)/5)) % 3 == 0:
    print(int((a-3)/5)+(a-5*int((a-3)/5))//3)
else:
    print(-1)