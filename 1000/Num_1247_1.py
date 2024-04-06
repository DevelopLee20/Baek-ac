lst = []

lst.append(sum(list(map(int,input().split()))))
lst.append(sum(list(map(int,input().split()))))
lst.append(sum(list(map(int,input().split()))))

for i in lst:
    if i == 3:
        print('A')
    elif i == 2:
        print('B')
    elif i == 1:
        print('C')
    elif i == 4:
        print('E')
    else:
        print('D')